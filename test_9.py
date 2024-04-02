from solution_9 import StrandsDNA

gen = StrandsDNA()
gen.add_strands('GHFUS DJGNDS AM FNSKOFE ASDJPV ASGSAZD')
print(gen)
gen.add_strands('GJSU EWJFSN FNSKOFE')
gen.add_strands('FHCNRU ALPFUR')
print(gen)
print(gen.get_max_strands())
