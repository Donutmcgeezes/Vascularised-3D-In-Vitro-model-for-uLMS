input = getDirectory("Choose input folder");
output = getDirectory("Choose output folder");
list = getFileList(input);

// count total .tif files first so we can show progress as "x of N"
total = 0;
for (i = 0; i < list.length; i++) {
    if (endsWith(list[i], ".tif")) total++;
}

print("\\Clear");
print("Found " + total + " .tif files to process.");
start = getTime();

count = 0;
setBatchMode(true);
for (i = 0; i < list.length; i++) {
    if (endsWith(list[i], ".tif")) {
        count++;
        print("[" + count + "/" + total + "] Processing: " + list[i]);
        open(input + list[i]);
        run("Subtract Background...", "rolling=50 stack");
        name = substring(list[i], 0, lengthOf(list[i]) - 4);
        outName = name + "-SB.tif";
        saveAs("Tiff", output + outName);
        close();
        print("  → Saved as: " + outName);
    }
}
setBatchMode(false);

elapsed = (getTime() - start) / 1000;
print("All done. Processed " + count + " of " + total + " files in " + elapsed + " seconds.");