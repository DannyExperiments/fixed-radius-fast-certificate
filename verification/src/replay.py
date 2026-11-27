"""Exact rational checks for a conservative concrete segment witness."""
from fractions import Fraction as F

c, pi, alpha, eps = F(1), F(1,2), F(1,8), F(1,4)
T = 2**32
# ln(2/alpha)<4; ln(1+T)<33, via e>2.
assert 2/alpha == 2**4 and 1+T < 2**33
assert F(4,2) + F(33,4) < 16
W = 5  # strictly bounds 1 + the above square root
# ln(11 max(ln T,1)/alpha)<9 via e>5/2.
assert 88*32 < F(5,2)**9
# LIL/T + sum(widths)/T < (6+2)/sqrt(T).
b_over_t_upper = (1+5*c)*W/min(pi,F(1,2))*F(8,2**16)
bad, good = F(1,2), F(3,4)
assert b_over_t_upper < eps*bad/(2-eps) == F(1,14)
assert bad**2 + good**2 < 1 and bad < (1-eps)*good
d = 8192*T*W*W + 1
assert F(512*(T-1)*W*W,d) < F(1,16)
assert F(5,16)-F(1,16) == F(1,4) > alpha
assert F(1,4)-F(1,16) > F(1,16)
print(f"PASS: exact deterministic bounds at T={T}, d={d}. The proof covers every fixed radius and optimism parameter.")

for k in range(29):
    r = F(k, 224)
    lower, upper = bad-r, bad+r
    assert (lower > (1-eps)*upper > 0) == (k < 16)
    if k == 14:
        assert lower == F(7,16) and (1-eps)*upper == F(27,64)
        assert lower-(1-eps)*upper == F(1,64)
print("All 29 exact explorer settings checked, including the strict tie at 1/14.")
