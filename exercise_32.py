pipe_lengths = [2.5, 3.0, 0.4, 5.2, 1.2, 0.3, 4.0]
def analyze_pipe_network(length):
    finle_length=0
    pipe_counts=len(length)
    short_pipe=False
    for pipe in length:
        finle_length+=pipe
        if pipe<0.5:
            short_pipe=True
    return finle_length,short_pipe,pipe_counts
F,SH_P,P_C=analyze_pipe_network(pipe_lengths)
print(f"Total Length:{F},System Report: {SH_P}, Total Pipes: {P_C}")
if SH_P==True:
    print("Warning: Very short pipes detected in the system! Check installation limits.")
else:
    "Pass: All pipes are standard length."