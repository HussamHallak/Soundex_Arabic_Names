# Create a grouped barplot and add a legend
Libindic_Soundex <- c(P=0.961, R=0.802, TNR=0.999, F=0.874, ACC=0.996, BA=0.901)
Jellyfish_Soundex <- c(P=0.963, R=0.833, TNR=0.999, F=0.894, ACC=0.997, BA=0.917)
Jellyfish_Match_Rating <- c(P=0.988, R=0.657, TNR=0.999, F=0.789, ACC=0.995, BA=0.828)
Fuzzy_NYSIIS <- c(P=0.982, R=0.429, TNR=1.0, F=0.597, ACC=0.991, BA=0.714)
Fuzzy_DMetaphone <- c(P=0.934, R=0.811, TNR=0.999, F=0.868, ACC=0.996, BA=0.905)
all <- rbind(Libindic_Soundex, Jellyfish_Soundex, Jellyfish_Match_Rating, Fuzzy_NYSIIS, Fuzzy_DMetaphone)
barplot(all, beside = TRUE, main = "Metrics based on both directions names matching using phonetic algorithms", xlab = "Metric", ylim = c(0,1), ylab = "Value", col = c("dodgerblue3", "black", "orange", "skyblue1", "red"), legend.text = rownames(all),  xlim = c(0,55), args.legend = list(cex=0.8,x = "topright"))
