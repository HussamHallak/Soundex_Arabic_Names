# Create a grouped barplot and add a legend
Libindic_Soundex <- c(P=0.825, R=0.952, TNR=0.997, F=0.884, ACC=0.996, BA=0.975)
Levenshtine_Distance <- c(P=0.865, R=0.623, TNR=0.998, F=0.725, ACC=0.992, BA=0.811)
Jellyfish_Soundex <- c(P=0.823, R=0.955, TNR=0.997, F=0.884, ACC=0.996, BA=0.976)
Jellyfish_Match_Rating <- c(P=0.988, R=0.641, TNR=1.0, F=0.777, ACC=0.994, BA=0.820)
Fuzzy_NYSIIS <- c(P=0.924, R=0.749, TNR=0.999, F=0.828, ACC=0.995, BA=0.874)
Fuzzy_DMetaphone <- c(P=0.904, R=0.994, TNR=0.998, F=0.947, ACC=0.998, BA=0.996)
all <- rbind(Libindic_Soundex, Levenshtine_Distance, Jellyfish_Soundex, Jellyfish_Match_Rating, Fuzzy_NYSIIS, Fuzzy_DMetaphone)
barplot(all, beside = TRUE, main = "Metrics based on one direction names matching using phonetic algorithms", xlab = "Metric", ylim = c(0,1), ylab = "Value", col = c("dodgerblue3", "green", "black", "orange", "skyblue1", "red"), legend.text = rownames(all),  xlim = c(0,55), args.legend = list(cex=0.8,x = "topright"))
