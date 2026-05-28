import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import os

folder_path = f'D:/MEng Project/Bella Chips/3. HUVECs Fibroblasts/VESNA analysis/output1'
filenames = os.listdir(folder_path)
print(filenames)

A = pd.read_csv(folder_path+'/file_names.csv')
sample_num = len(A)

# Create a subfolder for the plots
plots_dir = folder_path + '/plots'
os.makedirs(plots_dir, exist_ok=True)

# Containers for overview plots
vb_by_sample = {}   # branches-per-skeleton data
bi_by_sample = {}   # segment length data
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
    
     # Save data for overview plots later
    vb_by_sample[i+1] = VBranches
    bi_by_sample[i+1] = BranchInfo

    # ============================================================
    # PER-SAMPLE PLOTS
    # ============================================================

    # --- Branches per skeleton (log-log histogram) ---
    branches = VBranches['# Branches'].values
    fig, ax = plt.subplots(figsize=(8, 5))
    max_br = max(int(branches.max()), 2)
    bins = np.logspace(0, np.log10(max_br + 1), 30)
    ax.hist(branches, bins=bins, edgecolor='black', alpha=0.75, color='steelblue')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Branches per skeleton (log scale)')
    ax.set_ylabel('Number of skeletons (log scale)')
    ax.set_title(f"Sample {i+1} — branches per skeleton\n"
                 f"n={len(branches)} skeletons, "
                 f"median={int(np.median(branches))}, max={int(branches.max())}")
    ax.axvline(20, color='red', linestyle='--', alpha=0.6,
               label='20-branch threshold')
    ax.text(0.97, 0.95,
            f"1-branch skeletons: {n_components_single}\n"
            f">20-branch skeletons: {n_components_substantial}",
            transform=ax.transAxes, ha='right', va='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(plots_dir + f'/branches_per_skeleton_sample_{i+1}.png', dpi=150)
    plt.close(fig)

     # --- Segment length (linear histogram) ---
    lengths = BranchInfo['Branch length'].values
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(lengths, bins=40, edgecolor='black', alpha=0.75, color='seagreen')
    ax.axvline(mean_seg_len, color='red', linestyle='--',
               label=f'Mean = {mean_seg_len:.1f} µm')
    ax.axvline(median_seg_len, color='orange', linestyle='--',
               label=f'Median = {median_seg_len:.1f} µm')
    ax.set_xlabel('Segment length (µm)')
    ax.set_ylabel('Number of segments')
    ax.set_title(f"Sample {i+1} — segment length distribution\n"
                 f"n={len(lengths)} segments, max={lengths.max():.1f} µm")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(plots_dir + f'/segment_length_sample_{i+1}.png', dpi=150)
    plt.close(fig)

    # ============================================================
    # OVERVIEW PLOTS (all samples combined)
    # ============================================================

    colors = plt.cm.tab10(np.linspace(0, 1, max(len(vb_by_sample), 3)))

    # --- Branches per skeleton: overlaid histogram + complementary CDF ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    all_br = np.concatenate([vb['# Branches'].values for vb in vb_by_sample.values()])
    max_br = max(int(all_br.max()), 2)
    bins = np.logspace(0, np.log10(max_br + 1), 25)

    for (sample_id, vb), color in zip(vb_by_sample.items(), colors):
        br = vb['# Branches'].values
        ax1.hist(br, bins=bins, alpha=0.45,
                label=f'Sample {sample_id}', color=color, edgecolor=color)
        sorted_br = np.sort(br)
        ccdf = 1.0 - np.arange(len(sorted_br)) / len(sorted_br)
        ax2.plot(sorted_br, ccdf, label=f'Sample {sample_id}',
                color=color, linewidth=2)
        
    ax1.set_xscale('log'); ax1.set_yscale('log')
    ax1.set_xlabel('Branches per skeleton (log scale)')
    ax1.set_ylabel('Number of skeletons (log scale)')
    ax1.set_title('Branches-per-skeleton distribution')
    ax1.axvline(20, color='red', linestyle='--', alpha=0.5)
    ax1.legend(); ax1.grid(True, alpha=0.3)

    ax2.set_xscale('log'); ax2.set_yscale('log')
    ax2.set_xlabel('Branches per skeleton (log scale)')
    ax2.set_ylabel('P(X ≥ x)')
    ax2.set_title('Complementary CDF — tail comparison')
    ax2.legend(); ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(plots_dir + '/branches_per_skeleton_overview.png', dpi=150)
    plt.close(fig)

    # --- Segment length: overlaid density + boxplot ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    all_lens = np.concatenate([bi['Branch length'].values for bi in bi_by_sample.values()])
    bins = np.linspace(0, np.percentile(all_lens, 99), 40)

    for (sample_id, bi), color in zip(bi_by_sample.items(), colors):
        lens = bi['Branch length'].values
        ax1.hist(lens, bins=bins, alpha=0.45, density=True,
                label=f'Sample {sample_id}', color=color, edgecolor=color)

    ax1.set_xlabel('Segment length (µm)')
    ax1.set_ylabel('Density')
    ax1.set_title('Segment-length distribution (density)')
    ax1.legend(); ax1.grid(True, alpha=0.3)

    data = [bi['Branch length'].values for bi in bi_by_sample.values()]
    labels = [str(s) for s in bi_by_sample.keys()]
    bp = ax2.boxplot(data, tick_labels=labels, showfliers=False, patch_artist=True)
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)
    ax2.set_xlabel('Sample')
    ax2.set_ylabel('Segment length (µm)')
    ax2.set_title('Segment length per sample (outliers hidden)')
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(plots_dir + '/segment_length_overview.png', dpi=150)
    plt.close(fig)

    
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