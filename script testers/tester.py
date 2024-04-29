def calculate_N_canal(F_central):
    N_canal = int((F_central - 473000000) / 6000000) + 14
    return N_canal

# Test the function with F_central = 527142857
F_central = 539142857
N_canal = calculate_N_canal(F_central)
print("For F_central =", F_central, "N_canal is approximately:", N_canal)
