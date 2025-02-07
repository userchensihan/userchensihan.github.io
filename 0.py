
from manim import *
class AnimatingMethods(Scene):
    def construct(self):
        T=MathTex(r"\int_{}^{}sinxe^{sinx}\mathrm{d}x\\",font_size=50)

        self.play(Write(T),run_time=1.5)
        self.wait()
        self.remove(T)
        S=MathTex(r"\int_{0}^{\infty}\frac{sinx}{x}ln(1+x)\mathrm{d}x")

        self.play(Write(S),run_time=1.6)
        self.wait()
        self.remove(S)
        U=MathTex(r"\int_{0}^{1}\frac{\mathrm{Li}_{2}(-x)-\mathrm{Li_{2}(1-x)+\ln(x)\ln(1+x)+\pi x\ln(1+x)-\pi x\ln(x)}}{1+x^2}\frac{\mathrm{d}x}{\sqrt{1-x^2}}",font_size=30)
        self.play(Write(U),run_time=2.3)
        
        self.wait()
        self.remove(U)
        G=MathTex(r"e^{\gamma^\pi}>e+\phi-\pi")
        self.play(Write(G),run_time=1.2)
        self.wait()
        
