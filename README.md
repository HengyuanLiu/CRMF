<style>
img {
    display: block;
    margin: 0 auto;
}
p.center {text-align:center;}
</style>

# CRMF: Software Fault Localization based on Class Reduction and Method Call Frequency
The Code Repository of CRMF (a method call frequency based fault localization technique).
CRMF is a fault localization technique based on class reduction and method call frequency, that utilizes mutation analysis and information retrieval technique.


## Workflow of CRMF
The framework consists of two phases: reduction for class (RFC) and calculation for suspiciousness (CFS). 
In the RFC phase, CRMF filters classes with a higher probability of being faulty reduced classes set and records the method call frequency when the tests execute the program.
Then, in the CFS phase, CRMF utilizes an information retrieval based formula MFSF to compute the method's suspiciousness in reduced classes set. Finally, CRMF generates a ranking list of the target methods based on the suspiciousness.
<img src=https://www.hualigs.cn/image/61d4410445528.jpg width=50%>
<p class="center">Figure 1. Workflow of CRMF</p>

## Workflow of RFC
The RFC phase contains two steps: class mutation and class reduction. In the class mutation step, the classes covered by failed tests are mutated based on the mutation analysis. And in the class reduction step, we first compute the two distances (i.e., Mutant Distance and Class Distance). Then, we reduce the class with a lower probability to be faulty by utilizing Chebyshev's theorem.
<img src=https://www.hualigs.cn/image/61d452409e798.jpg width=50%>
<p class="center">Figure 2. Workflow of RFC</p>


