# Balart_Garcia_et_al_2021_MolecularEcology

Smelling in the dark: phylogenomic insights into the chemosensory system of a subterranean beetle

Pau Balart-García, Alexandra Cieslak,  Paula Escuer, Julio Rozas, Ignacio Ribera, Rosa Fernández

SUPPORTING MATERIAL ONLINE

1. Fastq_files: Trimmed data fastqc report.

2. Transcriptome_assembly: output of Trinity assembly.

3. Decontamination: output of Blobtools decontamination using Blastp annotations (following section)

4. Annotations: output of Blastp searches used implemented in Blobtools (Sl_ab_orfs.blastp.outfmt6) and  eggNOG-mapper output used for the Gene Ontology based analyses (Sl_ab_orfs.emapper.annotations).

5. Transcript_quantification: output of Salmon, expression quantification for each of the replicates (Sl_*_rep*) and expression matrices of genes and isoforms (Quantification_Sl) containing not-normalized expression values (counts and TPM) and normalized expression values (TMM).

6. Differential_expression_analyses: Differential expression results at gene level for all the transcriptome (All_transcriptome) and extracting only the genes with chemosensory functions (Subset_Chemosensory_Genes) annotated with Bitacora (section 8).

7. ORFs: predicted open reading frames (ORF) with Transdecoder.

8. Bitacora_annotation: Databases (DBs_query_chemo) used as query for Bitacora annotation (fasta and hmm files), initial annotations obtained with Bitacora protein mode and the Perl script used for executing this module (Raw-hits_and_script) and final chemosensory gene candidates after manual validation in a single fasta file including custom Python script to select the longest isoform of each gene using Transdecoder headings (Final_candidates).

9. Phylogenies: A folder per chemosensory gene family/subfamily containing the used sequences (*sequences.fasta), the alignment (*pasta.aln), trimmed alignment (*trimal.fasta), the guide tree (*guidetree.treefile) and the IQTREE output in nexus format (*IQTREE.treefile).
