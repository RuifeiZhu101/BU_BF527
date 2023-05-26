library("stats")

### Define our heat map function
make_heat_map <- function(dat,plot_name){
  
  ### Set row and column clustering for heatmap.
  ### Method "ward" may be "ward.D" depeding on version of hclust and stats
  hclust_col <- hclust(dist(t(dat)),method="ward")
  hclust_row <- hclust(as.dist(1-cor(t(dat))),method="ward")
  
  png(filename = paste0(plot_name,'.png'))
  ### Run R's built-in heatmap function to plot the matrix
  heatmap(dat,
          Rowv = as.dendrogram(hclust_row),
          Colv = as.dendrogram(hclust_col),
          cexCol = 0.75,
          main = plot_name,
          labRow = "",
          scale = "row")
  dev.off()
  cat("Done!\n")
}

### Read in the count table and DESeq2 differential expression results files
read_counts = read.table("Lab_19_count_table.txt",header = T,check.names=F, stringsAsFactors=F, row.names=1)
de_results_DESeq = read.table("Lab_19_DE_results_DESeq.txt",header = T,check.names=F, stringsAsFactors=F, row.names=1)
de_results_edgeR = read.table("Lab_19_DE_results_edgeR.txt",header = T,check.names=F, stringsAsFactors=F, row.names=1)
read_counts = read_counts[rowSums(read_counts) != 0,]

### Example code to perform differential expression analysis with EdgeR, requires EdgeR package
# group = c(rep("Fatal", 3) , rep("Survivor", 3))
# cds = DGEList(read_counts,group=group)
# cds = cds[rowSums(1e+06 * cds$counts/expandAsMatrix(cds$samples$lib.size, dim(cds)) > 1) >= 3, ]
# cds = calcNormFactors( cds )
# cds = estimateCommonDisp( cds )
# de.cmn = exactTest( cds , pair = c( "Fatal" , "Survivor" ) )
# resultsTable = topTags( de.cmn , n = nrow( de.cmn$table ) )$table

### Convert read_counts from R dataframe to matrix object
read_counts = as.matrix(read_counts)

### Normalize read_counts based on total number of reads per sample
#cat("Normalizing read counts ..\n")
#normalization_factors <- colSums(read_counts)
#normalization_factors <- mean(normalization_factors)/normalization_factors
#read_counts <- read_counts * normalization_factors

### Run heat map of full set of genes in dataset
cat("Plotting heatmap ..\n")
make_heat_map(read_counts,'Heatmap_all_genes_no_normalization')

### What do you think these lines accomplish?
de_genes_edgeR = de_results_edgeR[which(de_results_edgeR$FDR < 0.05 & abs(de_results_edgeR$logFC) > 5),]
de_genes_deSEQ = de_results_DESeq[which(de_results_DESeq$padj < 0.05 & abs(de_results_DESeq$log2FoldChange) > 5),]


### Write table of DE genes to a file for further analysis
write.table(rownames(de_genes_deSEQ),"DE_genes_deSEQ.txt",row.names=F,col.names=F,quote=F)
write.table(rownames(de_genes_edgeR),"DE_genes_edgeR.txt",row.names=F,col.names=F,quote=F)
