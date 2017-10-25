TABLE = '\t\t\tActual\tTheory\t| Residual\nMean\t\t{0:.4f}\t{2:.4f}\t| {4:.2E}\nVariance\t{1:.4f}\t{3:.4f}\t| {5:.2E}'


def print_table(actual, theory_mean, theory_var):
    mean_diff = abs(actual.mean() - theory_mean)
    var_diff = abs(actual.var() - theory_var)
    print(TABLE.format(actual.mean(), actual.var(), theory_mean, theory_var, mean_diff, var_diff))
    print('---' * 25)
