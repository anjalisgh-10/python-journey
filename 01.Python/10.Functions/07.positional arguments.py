def calculate_marks(maths, eng, hindi, comp, history):
    print(f"maths = {maths}")
    print(f"eng = {eng}")
    print(f"hindi = {hindi}")
    print(f"comp = {comp}")
    print(f"history = {history}")
    total_marks = maths + eng + hindi + comp + history
    print(f"Total marks scored = {total_marks}")


calculate_marks(hindi=22, maths=11, history=99, comp=56, eng= 99)