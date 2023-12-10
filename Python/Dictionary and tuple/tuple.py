# tuples are immutable
def find_pe_and_pb(price,eps,book_value):
    pe=price/eps
    pb=price/book_value
    return [pe,pb]

pe_ratio,pb_ratio = find_pe_and_pb(100,2,4)
print(f"{pe_ratio} {pb_ratio}")

def find_pe_and_pb(price,eps,book_value):
    pe=price/eps
    pb=price/book_value
    return (pe,pb)   # return pe,pb is same as return (pe,pb)

pe_ratio,pb_ratio = find_pe_and_pb(100,2,4)
print(f"{pe_ratio} {pb_ratio}")