import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import os

folder_path = f'D:/MEng Project/Bella Chips/1. HUVECs/290426/VESNA analysis/outpu2'
filenames = os.listdir(folder_path)
print(filenames)

A = pd.read_csv(folder_path+'/file_names.csv')
sample_num = len(A)
all_results = []

for i in range(sample_num):
    print(i+1)
    BranchInfo = pd.read_csv(folder_path+f"/Branch information-{i+1}.csv")
    VBranches = pd.read_csv(folder_path+f"/Results Vascular Branches-{i+1}.csv")
    Vlength = pd.read_csv(folder_path+f"/Results Vascular Length-{i+1}.csv")
    VolFrac = pd.read_csv(folder_path+f"/Results Volume Fraction-{i+1}.csv")

    # ---------- Pull raw values ----------
    capillary_vol_um3 = float(VolFrac.iloc[0]['Volume'])   # µm³
    stack_vol_um3     = float(VolFrac.iloc[1]['Volume'])   # µm³
    vf_pct            = float(VolFrac.iloc[2]['Volume'])   # %
    stack_vol_mm3     = stack_vol_um3 / 1e9

    # ---------- Tier 1 ----------
    # Total network length (sum of every branch segment)
    total_len_um = BranchInfo['Branch length'].sum()
    total_len_mm = total_len_um / 1000
    length_density = total_len_mm / stack_vol_mm3  # mm per mm³

    # Branches, junctions, endpoints (summed across all skeletons)
    total_segments  = int(VBranches['# Branches'].sum())
    total_junctions = int(VBranches['# Junctions'].sum())
    total_endpoints = int(VBranches['# End-point voxels'].sum())
    total_triple    = int(VBranches['# Triple points'].sum())
    total_quad      = int(VBranches['# Quadruple points'].sum())
    bp_density      = total_junctions / stack_vol_mm3  # per mm³

    # Segment length stats
    mean_seg_len   = BranchInfo['Branch length'].mean()
    median_seg_len = BranchInfo['Branch length'].median()

    # Mean diameter from cylinder approximation: V = pi * r² * L
    mean_diam = 2 * math.sqrt(capillary_vol_um3 / (math.pi * total_len_um))

    # ---------- Tier 2 ----------
    # Endpoint-to-branchpoint ratio
    ep_bp_ratio = total_endpoints / total_junctions

    # Connectivity (each row of VBranches is one connected skeleton)
    n_components_total       = len(VBranches)
    n_components_single      = int((VBranches['# Branches'] == 1).sum())
    n_components_substantial = int((VBranches['# Branches'] > 20).sum())

    # Largest connected component
    largest_idx          = VBranches['# Branches'].idxmax()
    largest_n_branches   = int(VBranches.loc[largest_idx, '# Branches'])
    largest_len          = (VBranches.loc[largest_idx, '# Branches']* VBranches.loc[largest_idx, 'Average Branch Length'])
    largest_pct_of_total = largest_len / total_len_um * 100

    # Tortuosity = branch length / Euclidean distance between endpoints
    # Exclude loops (Euclidean=0) and degenerate cases (huge ratios from near-0 Euclidean)
    valid = BranchInfo[BranchInfo['Euclidean distance'] > 0]
    tort_all = valid['Branch length'] / valid['Euclidean distance']
    tort_filt = tort_all[tort_all < 100]
    tort_mean   = tort_filt.mean()
    tort_median = tort_filt.median()
    n_loops = int((BranchInfo['Euclidean distance'] == 0).sum())

    # ---------- Pack into a dict ----------
    all_results.append({
        'sample': i+1,
        # Stack
        'stack_volume_mm3': round(stack_vol_mm3, 6),
        'capillary_volume_um3': round(capillary_vol_um3, 1),
        # Tier 1
        'volume_fraction_pct': round(vf_pct, 3),
        'total_length_mm': round(total_len_mm, 3),
        'length_density_mm_per_mm3': round(length_density, 2),
        'total_segments': total_segments,
        'total_junctions': total_junctions,
        'bp_density_per_mm3': round(bp_density, 1),
        'mean_segment_length_um': round(mean_seg_len, 2),
        'median_segment_length_um': round(median_seg_len, 2),
        'mean_diameter_um': round(mean_diam, 2),
        # Tier 2
        'total_endpoints': total_endpoints,
        'ep_bp_ratio': round(ep_bp_ratio, 3),
        'n_components_total': n_components_total,
        'n_components_substantial_gt20': n_components_substantial,
        'n_components_single_branch': n_components_single,
        'largest_component_n_branches': largest_n_branches,
        'largest_component_pct_of_length': round(largest_pct_of_total, 2),
        'tortuosity_mean': round(tort_mean, 3),
        'tortuosity_median': round(tort_median, 3),
        'n_loops': n_loops,
        'triple_points': total_triple,
        'quadruple_points': total_quad,
    })

    print(f"  VF={vf_pct:.2f}%, L={total_len_mm:.2f} mm, "
          f"BPs={total_junctions}, segments={total_segments}, "
          f"⌀={mean_diam:.2f} µm, EP/BP={ep_bp_ratio:.2f}")

    
results_df = pd.DataFrame(all_results)

# Append MEAN and STD rows if multiple samples
if len(results_df) > 1:
    numeric_cols = results_df.select_dtypes(include='number').columns
    mean_row = {'sample': 'MEAN'}
    std_row  = {'sample': 'STD'}
    for col in numeric_cols:
        mean_row[col] = round(results_df[col].mean(), 3)
        std_row[col]  = round(results_df[col].std(), 3)
    results_df = pd.concat([results_df,
                            pd.DataFrame([mean_row, std_row])],
                           ignore_index=True)

output_path = folder_path + '/vesna_summary.csv'
results_df.to_csv(output_path, index=False)
print(f"\nWrote summary to: {output_path}")
print(results_df.to_string(index=False))