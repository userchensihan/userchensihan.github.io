from manim import *
class AnimatingMethods(Scene):
    def construct(self):

        A=r'x \notin y:=\neg x\in y'
        
        B=r'x \subseteq y:=\forall a:(a\in x \to a\in y)'
        C=r'x=y:=(x \subseteq y)\wedge(y \subseteq x)'
        D=r'x\ne y:=\neg(x=y)'
        E=r'x\subset y:=(x\subseteq y)\wedge(x \ne y)'
        F=r'(\exists!x:P(x)):=(\exists x:P(x))\wedge(\forall y:\forall z:P(y)\wedge P(z)\to y=z)'
        G=r'\exists y:\forall x:x\notin y\quad y:=\emptyset'

        H=r'\exists x:\emptyset\in x\wedge\forall y:(y\in x\to y\cup\{y\}\in x)\quad x:=\omega'
        I=r'\forall x:\forall y:\exists m:\forall u:(u \in m \leftrightarrow(u=x\vee u=y))\quad m:=\{x,y\}'
        J=r'\forall x:\exists u:\forall y: (y \in u \leftrightarrow \exists s:(y \in s \wedge s \in x))\quad u:=\bigcup x'
        K=r'\forall a:\forall x\in a:\exists!y:\psi(x,y)\to\exists b:\forall y:(y \in b\leftrightarrow\\\exists x:x\in a \wedge \psi(x,y))\quad b:=\psi(a)'
        L=r'\forall a:\exists b:\forall x:x\in b\leftrightarrow x\subseteq a\quad b:=2^a'
        M=r'\forall x:x\ne \emptyset\to\exists y:(y \in x\wedge y \cap x=\emptyset)'
        Q=r'\bigcap m:=\{x \in \bigcup m\mid\forall a:a\in m \to x\in a\}'
        Z=[A,B,C,D,E,F,G,H,I,J,K,L,M,Q]
        for k in Z:
            u=MathTex(k)
            self.play(Write(u),use_override=True)
            self.wait()
            
            
            self.wait()
            self.play(FadeOut(u))
        N=Text("Zermelo-Fraenkel set theory")
        self.add(N)
        self.wait()
            
        
        
        
        
