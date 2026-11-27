# Q966: Fixed-radius FAST can stop with a suboptimal certificate

## Theorem

For every fixed sphere radius c>0 and boundary optimism parameter π∈(0,1], there is an instance of the published Algorithm 1, with B(·)=c equal to the perturbation norm, ε=1/4 and required failure probability δ=1/8, where the procedure stops and outputs a point of true margin 1/2 although the optimum is 3/4, with probability at least 1/4. The action set may be a full-dimensional simplex, the feedback is noiseless, and there is one constraint. In particular its returned certificate cannot meet the promised requirements. The theorem also holds if the algorithm uses δ/5 internally instead of δ. It does not address inflated radius or a π shrinking with d.

## Published quantities

Use [Algorithm 1 (p. 5)](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gangrade25a/gangrade25a.pdf#page=5) and [Lemma 7 (p. 6)](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gangrade25a/gangrade25a.pdf#page=6). Write α for the internal confidence parameter (either δ or δ/5). For one constraint with true row vector θ, the predictable ridge matrix is V_t=I+Σ_{s<t} a_s a_sᵀ and θhat_t=V_t⁻¹Σ_{s<t}a_s S_s. The perturbed estimate is θhat_t+ω_t(α)V_t⁻¹ᐟ² ζ_t, where ζ_t is independent uniform on the sphere of radius c, and ω_t=1+√(ln(2/α)/2+ln(det V_t)/4). The chosen action maximizes this perturbed linear functional. The one-dimensional dual weight is exactly 1, so the statistic is T_t=Σ_{s≤t}S_s. The deterministic boundary on a fixed action history is

    b_t = (1+5c)ω_t / min(π,1/2) · [LIL(t,α)+Σ_{s≤t} ∥a_s∥_{V_s⁻¹}],
    LIL(t,α) = √(4t ln(11 max(ln(t),1)/α)).

Then U_t=(T_t+b_t)/t and L_t=(T_t−b_t)/t. Positive stopping occurs for L_t>(1−ε)U_t>0, with output the average of drawn actions and certificate L_t. Zero feedback noise obeys conditional centering and the sub-Gaussian requirement.

## Construction and proof

Set θ=(1/2,3/4,0,…,0). Its norm is √13/4<1. Use the convex hull of e₁,e₂ as the simplest example. For the full-dimensional version add 0 and η e_j, j=3,…,d, to those two vertices, with η>0 small as specified below. The vertex e₂ is optimal and the true margin of e₁ is 1/2, strictly below (1−ε)M*=9/16. The full-dimensional hull has d+1 affinely independent vertices and is contained in the Euclidean unit ball.

Let all played actions so far be e₁. Once there has been at least one sample, the ridge scores at e₁ and e₂ are (t−1)/(2t)≥1/4 and 0, respectively; the remaining vertex scores under the ridge estimate are zero. Along the all-e₁ history, det V_t=t and Σ_{s≤t}∥a_s∥_{V_s⁻¹}=Σ_{s≤t}s⁻¹ᐟ²≤2√t, so b_t/t tends to zero for fixed c,π,α, independently of d. Choose a finite integer T≥2 so that b_T/T<1/14 on this history. At T, the statistic per round is 1/2; the bound 1/14 is exactly the threshold for 1/2−b_T/T>(3/4)(1/2+b_T/T). Thus if no other action is played through T or until stopping, positive stopping occurs by T, and the returned average is e₁. No negative stopping is possible on this history.

Let W=1+√(ln(2/α)/2+ln(1+T)/4); then ω_t≤W for t≤T on that history. In any round 2≤t≤T with both first two perturbation coordinates in absolute value at most 1/(16W), the perturbed score of e₁ is at least 3/16 and that of e₂ is at most 1/16. For the full-dimensional version require η c W < 1/16; then all remaining perturbed scores are at most 1/16 on any such history, using the fixed norm directly. Consequently e₁ is the unique maximizer. A sphere coordinate has mean-square c²/d by symmetry and the deterministic squared norm. Markov's inequality and the union bound give

    P(any of these two coordinates exceeds 1/(16W) in rounds 2,…,T)
        ≤ 512(T−1)c²W²/d.

Draw the random directions on a virtual infinite trajectory even if the algorithm stops. Choose an integer d≥3 with d>8192 T c²W², making the last probability less than 1/16. In the segment example the first action is e₁ with probability 1/2 by exchangeability and continuity. For the full-dimensional example, the event ζ_{1,1}>max(0,ζ_{1,2}) has probability 3/8: the joint sign quadrants are equiprobable, and within the positive quadrant the coordinates are exchangeable without ties. Because ζ_{1,1} has a continuous distribution, choose η small enough that P(0<ζ_{1,1}≤η c)<1/16, as well as satisfying η≤1 and η c W<1/16. On ζ_{1,1}>max(0,ζ_{1,2},η c), every other perturbed vertex score is strictly lower at initialization. The first action is e₁ with probability at least 5/16, and the union bound gives probability at least 1/4 for e₁ initially and no later switch before T or stopping. All claims follow. In particular no number M_out can make 1/2≥M_out≥9/16 on this event.
