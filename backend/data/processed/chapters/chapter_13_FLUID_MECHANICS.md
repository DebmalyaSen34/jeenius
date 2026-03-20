## Chapter 13 FLUID MECHANICS

### 13.1 Fluids

Matter is broadly divided into three categories, solid, liquid and gas. The intermolecular forces are strong in solids, so that the shape and size of solids do not easily change. This force is comparatively less in liquids and so the shape is easily changed. Although the shape of a liquid can be easily changed, the volume of a given mass of a liquid is not so easy to change. It needs quite a good effort to change the density of liquids. In gases, the intermolecular forces are very small and it is simple to change both the shape and the density of a gas. Liquids and gases together are called fluids, i.e., that which can flow.

In this chapter we shall largely deal with liquids. The equations derived may be applicable to gases in many cases with some modifications. We shall assume that the liquids we deal with are _incompressible and nonviscous_. The first condition means that the density of the liquid is independent of the variations in pressure and always remains constant. The second condition means that parts of the liquid in contact do not exert any tangential force on each other. The force by one part of the liquid on the other part is perpendicular to the surface of contact. Thus, there is no friction between the adjacent layers of a liquid.

### 13.2 Pressure in a fluid

Consider a point \(A\) in the fluid (figure 13.1). Imagine a small area \(\Delta S\) containing the point \(A\). The fluid on one side of the area presses the fluid on the other side and vice versa. Let the common magnitude of the forces be \(F\). We define the pressure of the fluid at the point \(A\) as

\[P=\mathop{\rm Lim}\limits_{\Delta S\to 0}\ \frac{F}{\Delta S}\\[F_{1} =P\;\Delta S\] and \[F_{2} =(P+dP)\Delta S.\]

The volume of the fluid considered is \((\Delta S)\,(dz)\). If the density of the fluid at \(A\) is \(\rho\), the mass of the fluid considered is \(\rho(\Delta S)\,(dz)\) and hence its weight \(W\) is

\[W =\rho\;(\Delta S)\,(dz)\,g.\]

For vertical equilibrium,

\[F_{1} =F_{2}+W\] or, \[P\;\Delta S =(P+dP)\,\Delta S+\rho\,g(dz)\,\Delta S\] or, \[dP =-\rho g\;dz\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \;It consists of two vertical cylinders \(A\) and \(B\) of different cross-sectional areas \(A_{1}\) and \(A_{2}\) connected by a horizontal tube. Pistons are fitted in both the cylinder. The load is kept on a platform fixed with the piston of larger area. A liquid is filled in the equipment. A valve \(V\) is fitted in the horizontal tube which allows the liquid to go from \(A\) to \(B\) when pressed from the \(A\)-side. The piston \(A\) is pushed by a force \(F_{1}\). The pressure in the liquid increases everywhere by an amount \(F_{1}/A_{1}\). The valve \(V\) is open and the liquid flows into the cylinder \(B\). It exerts an extra force \(F_{2}=A_{2}\left[\frac{F_{1}}{A_{1}}\right]\)on the larger piston in the upward direction which raises the load upward.

The advantage of this method is that if \(A_{2}\) is much larger than \(A_{1}\), even a small force \(F_{1}\) is able to generate a large force \(F_{2}\) which can raise the load. It may be noted that there is no gain in terms of work. The work done by \(F_{1}\) is same as that by \(F_{2}\). The piston \(A\) has to traverse a larger downward distance as compared to the height raised by \(B\).

### Atmospheric Pressure and Barometer

The atmosphere of the earth is spread up to a height of about 200 km. This atmosphere presses the bodies on the surface of the earth. The force exerted by the air on any body is perpendicular to the surface of the body. We define _atmospheric pressure_ as follows. Consider a small surface \(\Delta S\) in contact with air. If the force exerted by the air on this part is \(F\), the atmospheric pressure is

\[P_{0}=\mathop{\rm Lim}\limits_{\Delta S\to 0}\frac{F}{\Delta S}\,.\]

Atmospheric pressure at the top of the atmosphere is zero as there is nothing above it to exert the force. The pressure at a distance \(z\) below the top will be \(\int\limits_{0}^{\int\limits_{0}^{\int\limits_{0}^{\int\limits_{0}^{\int\limits_ {0}^{\int\limits_{0}^{\int\limits_{0}^{\int\limits_{0}}}}}}}}\,\\[P =P_{0} +h\rho g\] \[=1 \cdot 01 \times 10^{{}^{5}}\,\text{Pa}+(0 \cdot 20\text{ m})\,(1000\text{ kg m}^{{}_{\text{3}}})\,(10\text{ m s}^{{}_{\text{2}}})\] \[=1 \cdot 01 \times 10^{{}^{5}}\,\text{Pa}+0 \cdot 02 \times 10^{{}^{5}}\,\text{Pa}\] \[=1 \cdot 03 \times 10^{{}^{5}}\,\text{Pa}.\]

The area of the bottom \(=\pi\,r^{{}^{2}}=3 \cdot 14 \times(0 \cdot 1\text{ m})^{{}^{2}}\)

\[=0 \cdot 0314\text{ m}^{{}^{2}}.\]

The force on the bottom is, therefore,

\[F =P\,\pi\,r^{{}^{2}}\] \[=(1 \cdot 03 \times 10^{{}^{5}}\,\text{Pa}) \times(0 \cdot 0314\text{ m}^{{}^{2}}) =3230\text{ N}.\]

#### **Manometer**

Manometer is a simple device to measure the pressure in a closed vessel containing a gas. It consists of a U-tube having some liquid. One end of the tube is open to the atmosphere and the other end is connected to the vessel (figure 13.7).

The pressure of the gas is equal to the pressure at \(A\)

\[=\text{ pressure at}\,B\] \[=\text{ pressure at}\,C+h\rho g\] \[=P_{0} +h\rho g\]

when \(P_{0}\) is the atmospheric pressure, \(h = BC\) is the difference in levels of the liquid in the two arms and \(\rho\) is the density of the liquid.

The excess pressure \(P -P_{0}\) is called the _quage pressure_.

#### **13.5** Archimedes'** principle

When a body is partially or fully dipped into a fluid, the fluid exerts forces on the body. At any small portion of the surface of the body, the force by the fluid is perpendicular to the surface and is equal to the pressure at that point multiplied by the area (figure 13.8). The resultant of all these contact forces is called the force of _buoyancy_ or _buoyant force_.

Archimedes' principle states that _when a body is partially or fully dipped into a fluid at rest, the fluid exerts an upward force of buoyancy equal to the weight of the displaced fluid_.

Archimedes' principle is not an independent principle and may be deduced from Newton's laws of motion.

Consider the situation shown in figure (13.8) where a body is shown dipped into a fluid. Suppose the body dipped in the fluid is replaced by the same fluid of equal volume. As the entire fluid now becomes homogeneous, all parts will remain in equilibrium. The part of the fluid substituting the body also remains in equilibrium. Forces acting on this substituting fluid are

* the weight _mg_ of this part of the fluid, and
* the resultant \(B\) of the contact forces by the remaining fluid.

As the substituting fluid is in equilibrium, these two should be equal and opposite. Thus,

\[B =mg\qquad\qquad\qquad... \tag{13.5}\]

and it acts in the vertically upward direction.

Now the substituting fluid just occupies the space which was previously occupied by the body. Hence, the shape of the boundary of the substituting fluid is same as the boundary of the body. Thus, the magnitude and direction of the force due to the pressure on any small area of the boundary is same for the body as for the substituting fluid. The force of buoyancy on the body is, therefore, same as the force of buoyancy \(B\) on the substituting fluid.

From equation (13.5) the force of buoyancy on a dipped body is equal to the weight _mg_ of the displaced fluid and acts along the vertically upward direction. This is Archimedes' principle.

Note that in this derivation we have assumed that the fluid is in equilibrium in an inertial frame. If it is not so, the force of buoyancy may be different from the weight of the displaced fluid.

#### **Floatation**

When a solid body is dipped into a fluid, the fluid exerts an upward force of buoyancy on the solid. If the force of buoyancy equals the weight of the solid, the solid will remain in equilibrium. This is called _floatation_. When the overall density of the solid is smaller than the density of the fluid, the solid floats with a part of it in the fluid. The fraction dipped is such that the weight of the displaced fluid equals the weight of the solid.

Figure 13.8:

**Example 13.2**:

_A 700_ _g solid cube having an edge of length_ 10 cm _floats in water. How much volume of the cube is outside the water_? _Density of water_ = 1000 kg m-3.
**Solution :**: The weight of the cube is balanced by the buoyant force. The buoyant force is equal to the weight of the water displaced. If a volume \(V\) of the cube is inside the water, the weight of the displaced water = \(V_{g}\), where \(r\) is the density of water. Thus,

\[V_{\text{P}}g = (0 \cdot 7\text{ kg})\,g\]

or,

\[V = \frac{0 \cdot 7\text{ kg}}{\rho} = \frac{0 \cdot 7\text{ kg}}{1000\text{ kg m}^{ - 3}} = 7 \times 10 ^{ - 4}\text{ m}^{ 3} = 700\text{ cm}^{ 3}\text{.}\]

The total volume of the cube = (10 cm) 3 = 1000 cm 3. The volume outside the water is

1000 cm 3 - 700 cm 3 = 300 cm 3.

### Pressure difference and buoyant force in accelerating fluids

Equations (13.3) and (13.5) were derived by assuming that the fluid under consideration is in equilibrium in an inertial frame. If this is not the case, the equations must be modified. We shall discuss some special cases of accelerating fluids.

## A Liquid Placed in an Elevator

### Pressure Difference

Suppose a beaker contains some liquid and it is placed in an elevator which is going up with an acceleration \(a\)0 (figure 13.9). Let \(A\) and \(B\) be two points in the liquid, \(B\) being at a vertical height \(z\) above \(A\). Construct a small horizontal area D_S_ around \(A\) and an equal horizontal area around \(B\). Construct a vertical cylinder with the two areas as the faces. Consider the motion of the liquid contained within this cylinder. Let \(P\)1 be the pressure at \(A\) and \(P\)2 be the pressure at \(B\).

Forces acting on the liquid contained in the cylinder, in the vertical direction, are :

1. \(P\)1D_S_, upward due to the liquid below it
2. \(P\)2D_S_, downward due to the liquid above it and
3. weight _mg_ = (D_S_)_z_pg_ downward, where \(r\) is the density of the liquid.

Under the action of these three forces the liquid is accelerating upward with an acceleration \(a\)0. From Newton's second law

\[P_{1}\Delta S - P_{2}\Delta S - mg = ma_{0}\] or, \[(P_{1} - P_{2})\Delta S = m(g + a_{0}) = (\Delta S)z\rho(g + a_{0})\] or, \[P_{1} - P_{2} = \rho(g + a_{0})z\text{ }\ldots\]
**(b) Buoyant Force**

Now suppose a body is dipped inside a liquid of density \(r\) placed in an elevator going up with an acceleration \(a\)0. Let us calculate the force of buoyancy \(B\) on this body. As was done earlier, let us suppose that we substitute the body into the liquid by the same liquid of equal volume. The entire liquid becomes a homogenous mass and hence the substituted liquid is at rest with respect to the rest of the liquid. Thus, the substituted liquid is also going up with an acceleration \(a\)0 together with the rest of the liquid.

The forces acting on the substituted liquid are

1. the buoyant force \(B\) and
2. the weight _mg_ of the substituted liquid. From Newton's second law

\[B - mg = ma_{0}\] or, \[B = m(g + a_{0}) \ldots\]

Equation (13.6) and (13.7) are similar to the corresponding equations for unaccelerated liquid with the only difference that \(g\) + \(a\) takes the role of \(g\).

### Free Surface of a Liquid in Horizontal Acceleration

Consider a liquid placed in a beaker which is accelerating horizontally with an acceleration \(a\)0 (figure 13.10). Let \(A\) and \(B\) be two points in the liquid at a separation \(l\) in the same horizontal line along the acceleration \(a\)0. We shall first obtain the pressure difference between the points \(A\) and \(B\).

Construct a small vertical area D_S_ around \(A\) and an equal area around \(B\). Consider the liquid contained in the horizontal cylinder with the two areas as the flat faces. Let the pressure at \(A\) be \(P\)1 and the pressure at \(B\) be \(P\)2. The forces along the line _AB_ are

1. \(P\)1D_S_ towards right due to the liquid on the left and
2. \(P\)2D_S_ towards left due to the liquid on the right.

Figure 13.10:Under the action of these forces, the liquid contained in the cylinder is accelerating towards right. From Newton's second law,

\[P_{1}\Delta S - P_{2}\Delta S = ma_{0}\] or, \[(P_{1} - P_{2})\Delta S = (\Delta S)\rho\sigma_{0}\] or, \[P_{1} - P_{2} = l\rho\sigma_{0}\;.\]

The two points in the same horizontal line do not have equal pressure if the liquid is accelerated horizontally.

As there is no vertical acceleration, the equation (13.3) is valid. If the atmospheric pressure is \(P_{0}\), the pressure at \(A\) is \(P_{1} = P_{0} + h_{1}\rho g\) and the pressure at \(B\) is \(P_{2} = P_{0} + h_{2}\rho g\), where \(h_{1}\) and \(h_{2}\) are the depths of \(A\) and \(B\) from the free surface. Substituting in (13.8)

\[h_{1}\rho g - h_{2}\rho g = l\rho a_{0}\] or, \[\frac{h_{1} - h_{2}}{l} = \frac{a_{0}}{g}\] or, \[\tan \theta = \frac{a_{0}}{g}\]

where \(\theta\) is the inclination of the free surface with the horizontal.

### Flow of Fluids

The flow of fluid is in general a complex branch of mechanics. If you look at the motion of water in a fall (like Rallah fall near Manali or Kemti fall near Moussurie) the view is very pleasant. The water falls from a height and then proceeds on a flat bed or a slope with thumping, jumping and singing if you can appreciate the music. But if you try to analyse the motion of each particle on the basis of laws of mechanics, the task is tremendously difficult. Other examples of fluid flow are the sailing of clouds and the motion of smoke when a traditional Chulha using coal, wood or goitha (prepared from cowdung) in an Indian village is lit. The motion of each smoke particle is governed by the same Newton's laws but to predict the motion of a particular particle is not easy.

### Steady and Turbulent Flow

Consider a liquid passing through a glass tube (figure 13.11). Concentrate on a particular point \(A\) in the tube and look at the particles arriving at \(A\). If the velocity of the liquid is small, all the particles which come to \(A\) will have same speed and will move in same direction. As a particle goes from \(A\) to another point \(B\), its speed and direction may change, but all the particles reaching \(A\) will have the same speed at \(A\) and all the particles reaching \(B\) will have the same speed at \(B\). Also, if one particle passing through \(A\) has gone through \(B\), then all the particles passing through \(A\) go through \(B\). Such a flow of fluid is called a _steady flow_.

In steady flow the velocity of fluid particles reaching a particular point is the same at all time. Thus, each particle follows the same path as taken by a previous particle passing through that point.

If the liquid is pushed in the tube at a rapid rate, the flow may become turbulent. In this case, the velocities of different particles passing through the same point may be different and change erratically with time. The motion of water in a high fall or a fast flowing river is, in general, turbulent.

Steady flow is also called _streamline flow_.

#### Line of Flow : Streamline

The path taken by a particle in flowing fluid is called its _line of flow_. The tangent at any point on the line of flow gives the direction of motion of that particle at that point. In the case of steady flow, all the particles passing through a given point follow the same path and hence we have a unique line of flow passing through a given point. In this case, the line of flow is also called a _streamline_. Thus, the tangent to the streamline at any point gives the direction of all the particles passing through that point. It is clear that two streamlines cannot intersect, otherwise, the particle reaching at the intersection will have two different directions of motion.

#### Tube of Flow

Consider an area \(S\) in a fluid in steady flow. Draw streamlines from all the points of the periphery of \(S\). These streamlines enclose a tube, of which \(S\) is a cross-section. Such a tube is called a _tube of flow_. As the streamlines do not cross each other, fluid flowing through differnt tubes of flow cannot intermix, although there is no physical partition between the tubes. When a liquid is passed slowly through a pipe, the pipe itself is one tube of flow.

Figure 13.12

### 13.9 Irrotational flow of an incompressible and nonviscous fluid

The analysis of the flow of a fluid becomes much simplified if we consider the fluid to be incompressible and nonviscous and that the flow is irrotational. Incompressibility means that the density of the fluid is same at all the points and remains constant as time passes. This assumption is quite good for liquids and is valid in certain cases of flow of gases. Viscosity of a fluid is related to the internal friction when a layer of fluid slips over another layer. Mechanical energy is lost against such viscous forces. The assumption of a nonviscous fluid will mean that we are neglecting the effect of such internal friction. Irrotational flow means there is no net angular velocity of fluid particles. When you put some washing powder in a bucket containing water and mix it by rotating your hand in circular path along the wall of the bucket, the water comes into rotational motion. Quite often water flowing in rivers show small vortex formation where it goes in rotational motion about a centre. Now onwards we shall consider only the irrotational motion of an incompressible and nonviscous fluid.

### 13.10 Equation of continuity

We have seen that the fluid going through a tube of flow does not intermix with fluid in other tubes. The total mass of fluid going into the tube through any cross section should, therefore, be equal to the total mass coming out of the same tube from any other cross section in the same time. This leads to the equation of continuity.

Let us consider two cross sections of a tube of flow at the points \(A\) and \(B\) (figure 13.13). Let the area of cross section at \(A\) be \(A_{1}\) and that at \(B\) be \(A_{2}\). Let the speed of the fluid be \(v_{1}\) at \(A\) and \(v_{2}\) at \(B\).

\[\begin{array}{c}\includegraphics[scale=0.4]{figures/13.14}\end{array}\]

How much fluid goes into the tube through the cross section at \(A\) in a time interval \(\Delta t\)? Let us construct a cylinder of length \(v_{1}\Delta t\) at \(A\) as shown in the figure. As the fluid at \(A\) has speed \(v_{1}\), all the fluid included in this cylinder will cross through \(A_{1}\) in the time interval \(\Delta t\). Thus, the volume of the fluid going into the tube through the cross section at \(A\) is \(A_{1}v_{1}\Delta t\). Similarly, the volume of the fluid going out of the tube through the cross section at \(B\) is \(A_{2}v_{2}\Delta t\). If the fluid is incompressible, we must have

\[A_{1}v_{1}\Delta t =A_{2}v_{2}\,\Delta t\] \[\text{or,}\hskip 56.905512ptA_{1}v_{1} =A_{2}v_{2}\,. \tag{13.9}\]

_The product of the area of cross section and the speed remains the same at all points of a tube of flow._ This is called the _equation of continuity_ and expresses the law of conservation of mass in fluid dynamics.

_Figure (13.14) shows a liquid being pushed out of a tube by pressing a piston. The area of cross section of the piston is \(1\cdot 0\text{ cm}^{\text{\tiny 2}}\) and that of the tube at the outlet is \(20\text{ mm}^{\text{\tiny 2}}\). If the piston is pushed at a speed of \(2\text{ cm s}^{\text{\tiny 1}}\), what is the speed of the outgoing liquid_?

\[\begin{array}{c}\includegraphics[scale=0.4]{figures/13.14}\end{array}\]

_Solution :_ From the equation of continuity

\[A_{1}v_{1} =A_{2}v_{2}\] \[\text{or,}\hskip 14.226378pt(1\cdot 0\text{ cm}^{\text{\tiny 2}})(2\text{ cm s}^{\text{\tiny 1}})(2\text{ cm}^{\text{\tiny 2}})(20\text{ mm}^{\text{\tiny 2}})v_{2}\] \[\text{or,}\hskip 56.905512ptv_{2} =\frac{1\cdot 0\text{ cm}^{\text{\tiny 2}}}{20\text{ mm}^{\text{\tiny 2}}}\times 2\text{ cm s}^{\text{\tiny 1}}\] \[=\frac{100\text{ mm}^{\text{\tiny 2}}}{20\text{ mm}^{\text{\tiny 2}}}\times 2\text{ cm s}^{\text{\tiny 1}}=10\text{ cm s}^{\text{\tiny 1}}\,.\]

### 13.11 Bernoulli equation

Bernoulli equation relates the speed of a fluid at a point, the pressure at that point and the height of that point above a reference level. It is just the application of work-energy theorem in the case of fluid flow.

We shall consider the case of irrotational and steady flow of an incompressible and nonviscous liquid. Figure (13.15) shows such a flow of a liquid in a tube of varying cross section and varying height. Consider the liquid contained between the cross sections \(A\) and \(B\) of the tube. The heights of \(A\) and \(B\) are \(h_{1}\) and \(h_{2}\) respectively from a reference level. This liquid advances into the tube and after a time \(\Delta t\) is contained between the cross sections \(A^{\prime}\) and \(B^{\prime}\) as shown in figure.

Figure 13.15Suppose the area of cross section at \(A=A_{1}\) the area of cross section at \(B=A_{2}\) the speed of the liquid at \(A=v_{1}\) the speed of the liquid at \(B=v_{2}\) the pressure at \(A=P_{1}\) the pressure at \(B=P_{2}\) and the density of the liquid = \(\rho\).

The distance \(AA^{\prime}=v_{1}\Delta t\) and the distance \(BB^{\prime}=v_{2}\Delta t\). The volume between \(A\) and \(A^{\prime}\) is \(A_{1}v_{1}\Delta t\) and the volume between \(B\) and \(B^{\prime}\) is \(A_{2}v_{2}\Delta t\). By the equation of continuity,

\[A_{1}v_{1}\Delta t=A_{2}v_{2}\Delta t\;.\]

The mass of this volume of liquid is

\[\Delta m=\rho A_{1}v_{1}\Delta t=\rho A_{2}v_{2}\Delta t.\qquad\qquad...

Here \(h_{1} = h_{2}\). Thus,

\[P_{1} - P_{2} = \frac{1}{2}\,\rho v_{2}^{2} - \frac{1}{2}\,\rho v_{1}^{2}\] \[= \frac{1}{2} \times (1200\,\,{\rm kg}\,\,{\rm m}^{- 3})\,(2500\,\,{\rm cm}^{2}\,{\rm s}^{- 2} - 100\,\,{\rm cm}^{2}\,{\rm s}^{- 2})\] \[= 600\,\,{\rm kg}\,\,{\rm m}^{- 3} \times 2400\,\,{\rm cm}^{2}\,{\rm s}^{- 2} = 144\,\,{\rm Pa}.\]

#### Applications of Bernoulli equation

#### Hydrostatics

If the speed of the fluid is zero everywhere, we get the situation of hydrostatics. Putting \(v_{1} = v_{2} = 0\) in the Bernoulli equation (13.10)

\[P_{1} + \rho gh_{1} = P_{2} + \rho gh_{2}\] or, \[P_{1} - P_{2} = \rho g(h_{2} - h_{1})\]

as expected from hydrostatics.

#### Speed of Efflux

Consider a liquid of density \(r\) filled in a tank of large cross-sectional area \(A\)1. There is a hole of cross-sectional area \(A\)2 at the bottom and the liquid flows out of the tank through the hole. The situation is shown in figure (13.17). Suppose \(A_{2} << A_{1}\).

Let \(v_{1}\) and \(v_{2}\) be the speeds of the liquid at \(A\)1 and \(A\)2. As both the cross sections are open to the atmosphere, the pressures there equals the atmospheric pressure \(P\)0. If the height of the free surface above the hole is \(h\), Bernoulli equation gives

\[P_{0} + \frac{1}{2}\,\rho v_{1}^{2} + \rho gh = P_{0} + \frac{1}{2}\,\rho v_{2}^{2}\]

By the equation of continuity

\[A_{1}v_{1} = A_{2}v_{2}\]

. Putting \(v_{1}\) in terms of \(v_{2}\) in (i),

\[\frac{1}{2}\,\rho\left(\frac{A_{2}}{A_{1}} \right)^{2}\!\!v_{2}^{2} + \rho gh = \frac{1}{2}\,\rho v_{2}^{2}\] or, \[\left[ 1 - \left(\frac{A_{2}}{A_{1}} \right)^{2}\right]\!\!v_{2}^{2} = 2\,gh.\]

If \(A_{2} << A_{1}\), this equation reduces to \(v_{2}^{2} = 2\,gh\) or, \(v_{2} = \sqrt{2\,gh}\).

The speed of liquid coming out through a hole at a depth \(h\) below the free surface is the same as that of a particle fallen freely through the height \(h\) under gravity. This is known as _Torricelli's theorem_. The speed of the liquid coming out is called the _speed of efflux_.

#### Example 13.5

_A water tank is constructed on the top of a building. With what speed will the water come out of a tap_ 6*0 m _below the water level in the tank_? _Assume steady flow and that the pressure above the water level is equal to the atmospheric pressure._

_Solution_ : The velocity is given by Torricelli's theorem

\[v = \sqrt{2\,gh}\] \[= \sqrt{2\times(9\cdot 8\,\,{\rm m}\,\,{\rm s}^{- 2})\times(6\cdot 0\,\,{\rm m})} \simeq 11\,\,{\rm m}\,\,{\rm s}^{- 1}.\]

#### V Ventury Tube

A ventury tube is used to measure the flow speed of a fluid in a tube. It consists of a constriction or a throat in the tube. As the fluid passes through the constriction, its speed increases in accordance with the equation of continuity. The pressure thus decreases as required by Bernoulli equation.

Figure (13.18) shows a ventury tube through which a liquid of density \(r\) is flowing. The area of cross section is \(A\)1 at the wider part and \(A\)2 at the constriction. Let the speeds of the liquid at \(A\)1 and \(A\)2 be \(v\)1 and \(v\)2 and the pressures at \(A\)1 and \(A\)2 be \(P\)1 and \(P\)2 respectively. By the equation of continuity

\[A_{1}v_{1} = A_{2}v_{2}\]

and by Bernoulli equation,

\[P_{1} + \frac{1}{2}\,\rho v_{1}^{2} = P_{2} + \frac{1}{2}\,\rho v_{2}^{2}\] or, \[(P_{1} - P_{2}) = \frac{1}{2}\,\rho\left(v_{2}^{2} - v_{1}^{2}\right)\]

Figure (13.18) also shows two vertical tubes connected to the ventury tube at \(A\)1 and \(A\)2. If the difference in heights of the liquid levels in these tubes is \(h\), we have

\[P_{1} - P_{2} = \rho gh.\]

Figure 13.18:

Putting in (ii),

\[2\,gh={v_{2}^{2}}-{v_{1}^{2}}\qquad\qquad\qquad...\] (iii)

Knowing \(A_{1}\) and \(A_{2}\), one can solve equations (i) and (iii) so as to get \(v_{1}\) and \(v_{2}\). This allows one to know the rate of flow of liquid past a cross section.

### (d) Aspirator Pump

When a fluid passes through a region at a large speed, the pressure there decreases. This fact finds a number of useful applications. In an aspirator pump a barrel \(A\) terminates in a small constriction \(B\) (figure 13.19). A narrow tube \(C\) connects the constriction to a vessel containing the liquid to be sprayed. The air in the barrel \(A\) is pushed by the operator through a piston. As the air passes through the constriction \(B\), its speed is considerably increased and consequently the pressure drops. Due to reduced pressure in the constriction \(B\), the liquid is raised from the vessel and is sprayed with the expelled air.

### (e) Change of Plane of Motion of a Spinning Ball

Quite often when swing bowlers of cricket deliver the ball, the ball changes its plane of motion in air. Such a deflection from the plane of projection may be explained on the basis of Bernoulli equation.

Suppose a ball spinning about the vertical direction is going ahead with some velocity in the horizontal direction in otherwise still air. Let us work in a frame in which the centre of the ball is at rest. In this frame the air moves past the ball at a speed \(v\) in the opposite direction. The situation is shown in (13.20).

The plane of the figure represents horizontal plane. The air that goes from the \(A\) side of the ball in the figure is dragged by the spin of the ball and its speed increases. The air that goes from the \(B\) side of the ball in the figure suffers an opposite drag and its speed decreases. The pressure of air is reduced on the \(A\) side and is increased on the \(B\) side as required by the Bernoulli's theorem. As a result, a net force \(F\) acts on the ball from the \(B\) side to the \(A\) side due to this pressure difference. This force causes the deviation of the plane of motion.

### (f) Charge of Plane of Motion of a Spinning Ball

Quite often when swing bowlers of cricket deliver the ball, the ball changes its plane of motion in air. Such a deflection from the plane of projection may be explained on the basis of Bernoulli equation.

Suppose a ball spinning about the vertical direction is going ahead with some velocity in the horizontal direction in otherwise still air. Let us work in a frame in which the centre of the ball is at rest. In this frame the air moves past the ball at a speed \(v\) in the opposite direction. The situation is shown in (13.20).

The plane of the figure represents horizontal plane. The air that goes from the \(A\) side of the ball in the figure is dragged by the spin of the ball and its speed increases. The air that goes from the \(B\) side of the ball in the figure suffers an opposite drag and its speed decreases. The pressure of air is reduced on the \(A\) side and is increased on the \(B\) side as required by the Bernoulli's theorem. As a result, a net force \(F\) acts on the ball from the \(B\) side to the \(A\) side due to this pressure difference. This force causes the deviation of the plane of motion.

### (f) Charge of Motion of a Spinning Ball

Quite often when swing bowlers of cricket deliver the ball, the ball changes its plane of motion in air. Such a deflection from the plane of projection may be explained on the basis of Bernoulli equation.

Suppose a ball spinning about the vertical direction is going ahead with some velocity in the horizontal direction in otherwise still air. Let us work in a frame in which the centre of the ball is at rest. In this frame the air moves past the ball at a speed \(v\) in the opposite direction. The situation is shown in (13.20).

The plane of the figure represents horizontal plane. The air that goes from the \(A\) side of the ball in the figure is dragged by the spin of the ball and its speed increases. The air that goes from the \(B\) side of the ball in the figure suffers an opposite drag and its speed decreases. The pressure of air is reduced on the \(A\) side and is increased on the \(B\) side as required by the Bernoulli's theorem. As a result, a net force \(F\) acts on the ball from the \(B\) side to the \(A\) side due to this pressure difference. This force causes the deviation of the plane of motion.

### (f) Charge of Motion of a Spinning Ball

Quite often when swing bowlers of cricket deliver the ball, the ball changes its plane of motion in air. Such a deflection from the plane of projection may be explained on the basis of Bernoulli equation.

Suppose a ball spinning about the vertical direction is going ahead with some velocity in the horizontal direction in otherwise still air. Let us work in a frame in which the centre of the ball is at rest. In this frame the air moves past the ball at a speed \(v\) in the opposite direction. The situation is shown in (13.20).

Even Mount Everest (8848 m) would have been outside the atmosphere.

Figure 13.19:

**3.**: _The liquids shown in figure (13-WI) in the two arms are mercury (specific gravity =_ 13:6) and water. If the difference of heights of the mercury columns is_ 2 cm, _find the height_ \(h\) _of the water column._

**5.**: _The area of cross section of the two arms of a hydraulic press are_ 1 cm2  and 10 cm2 _respectively (figure 13-W3). A force of_ 5 N _is applied on the water in the thinner arm. What force should be applied on the water in the thicker arm so that the water may remain in equilibrium_?

**6.**: _A copper piece of mass_ 10 g _is suspended by a vertical spring. The spring elongates_ 1 cm _over its natural length to keep the piece in equilibrium. A beaker containing water is now placed below the piece so as to immerse the piece completely in water. Find the elongation of the spring. Density of copper =_ 9000 kg m-3._ _Take_ \(g\) = 10 m s-2.

**Solution :**: Let the spring constant be \(k\). When the piece is hanging in air, the equilibrium condition gives

\[\begin{array}{l}k(1\;{\rm cm})=(0\cdot 01\;{\rm kg})(10\;{\rm m}\;{\rm s}^{- 2})\end{array}\]

or \[\begin{array}{l}k(1\;{\rm cm})=0\cdot 1\;{\rm N}\;.\end{array}\]

The volume of the copper piece

\[\begin{array}{l}=\frac{0\cdot 01\;{\rm kg}}{9000\;{\rm kg}\;{\rm m}^{- 3}}=\frac{1}{9}\times 10^{- 5}\;{\rm m}^{3}.\end{array}\]

This is also the volume of water displaced when the piece is immersed in water. The force of buoyancy

\[\begin{array}{l}=\mbox{weight of the liquid displaced}\end{array}\]

\[\begin{array}{l}=\frac{1}{9}\times 10^{- 5}\;{\rm m}^{3}\times(1000\;{\rm kg}\;{\rm m}^{- 3})\times(10\;{\rm m}\;{\rm s}^{- 2})\end{array}\]

\[\begin{array}{l}=0\cdot 011\;{\rm N}.\end{array}\]

If the elongation of the spring is \(x\) when the piece is immersed in water, the equilibrium condition of the piece gives,

\[\begin{array}{l}kx=0\cdot 1\;{\rm N}-0\cdot 011\;{\rm N}=0\cdot 089\;{\rm N}. \end{array}\]

By (i) and (ii),

\[\begin{array}{l}x=\frac{0\cdot 089}{0\cdot 1}\;{\rm cm}=0\cdot 89\;{\rm cm}. \end{array}\]

**7.**: _A cubical block of wood of edge_ 3 cm _floats in water. The lower surface of the cube just touches the free end of a vertical spring fixed at the bottom of the pot. Find the maximum weight that can be put on the block without wetting it. Density of wood =_ 800 kg m-3 _and spring constant of the spring_ = 50 N m-1. _Take_ \(g\) = 10 m s-2.

Figure 13: W1

**Solution :**: The specific gravity of the block = 0*8. Hence the height inside water = 3 cm x 0*8 = 2*4 cm. The height outside water = 3 cm - 2*4 = 0*6 cm. Suppose the maximum weight that can be put without wetting it is \(W\). The block in this case is completely immersed in the water. The volume of the displaced water

= volume of the block = 27 x 10-6 m s.

Hence, the force of buoyancy

\[= (27 \times 10^{-6}\;{\text{m}}^{3}) \times (1000\;{\text{kg}}\;{\text{m}}^{3}) \times (10\;{\text{m}}\;{\text{s}}^{3})\] \[= 0\text{*}27\;{\text{N}}\;.\]

The spring is compressed by 0*6 cm and hence the upward force exerted by the spring

= 50 N m-1 x 0*6 cm = 0*3 N.

The force of buoyancy and the spring force taken together balance the weight of the block plus the weight \(w\) put on the block. The weight of the block is

\[W = (27 \times 10^{-6}\;{\text{m}}) \times (800\;{\text{kg}}\;{\text{m}}^{3}) \times (10\;{\text{m}}\;{\text{s}}^{2})\] \[= 0\text{*}22\;{\text{N}}\;.\]

Thus, \[w = 0\text{*}27\;{\text{N}} + 0\text{*}3\;{\text{N}} - 0\text{*}22\;{\text{N}}\] \[= 0\text{*}35\;{\text{N}}\;.\]
**8**: _A wooden plank of length 1_m_and uniform cross section is hinged at one end to the bottom of a tank as shown in figure (13-W5). The tank is filled with water up to a height of 0*5 m. The specific gravity of the plank is 0*5. Find the angle th that the plank makes with the vertical in the equilibrium position. (Exclude the case th = 0*0.)_

**Solution :**: The forces acting on the plank are shown in the figure. The height of water level is \(l\) = 0*5 m. The length of the plank is 1*0 m = 2\(l\). The weight of the plank acts through the centre \(B\) of the plank. We have _OB=l_. The buoyant force \(F\) acts through the point \(A\) which is the middle point of the dipped part _OC_ of the plank.

We have \[OA = \frac{OC}{2} = \frac{l}{2\;{\text{cos}}\theta}\;.\]

Let the mass per unit length of the plank be r.

Its weight _mg_ = 2_l_p_g.

The mass of the part _OC_ of the plank = \(\left( \frac{l}{{\text{cos}}\theta} \right)\)r.

The mass of water displaced = \(\frac{1}{0*5}\frac{l}{{\text{cos}}\theta} \rho = \frac{2l\rho}{{\text{cos}}\theta}\;.\)

The buoyant force \(F\) is, therefore, \(F = \frac{2l\rho g}{{\text{cos}}\theta}\;.\)

Now, for equilibrium, the torque of _mg_ about \(O\) should balance the torque of \(F\) about \(O\).

So, \(mg(OB)\text{sin}\theta = F(OA)\;{\text{sin}}\theta\)

or, \((2l\rho)l = \left( \frac{2l\rho}{{\text{cos}}\theta} \right)\left( \frac{l}{2\;{\text{cos}}\theta} \right)\)

or, \({\text{cos}}\theta = \frac{1}{2}\)

or, \({\text{cos}}\theta = \frac{1}{\sqrt{2}}\;,\;{\text{or}},\;\;\theta = 45^{\circ}\).
**9**: _A cylindrical block of wood of mass M is floating in water with its axis vertical. It is depressed a little and then released. Show that the motion of the block is simple harmonic and find its frequency._
**Solution :**: Suppose a height \(h\) of the block is dipped in the water in equilibrium position. If \(r\) be the radius of the cylindrical block, the volume of the water displaced = \(\pi r^{2}h\). For floating in equilibrium

\[\pi r^{2}h\rho g = W\between _A and B where the areas of cross section are_ 30 cm2 _and_ 15 cm2 _respectively. Find the rate of flow of water through the tube._

**Solution :**: Let the velocity at \(A\) = \(v_{A}\) and that at \(B\) = \(v_{B}\)

By the equation of continuity, \(\frac{v_{B}}{v_{A}} = \frac{30\text{ cm}^{2}}{15\text{ cm}^{2}} = 2\).

By Bernoulli equation,

\[P_{A} + \frac{1}{2}\varrho v_{A}^{2} = P_{B} + \frac{1}{2}\varrho v_{B}^{2}\]

or,

\[P_{A} - P_{B} = \frac{1}{2}\varrho\left(2\varrho_{A}\right)^{2} - \frac{1}{2}\varrho v_{A}^{2} = \frac{3}{2}\varrho v_{A}^{2}\]

or,

\[600\text{ N m}^{- 2} = \frac{3}{2}\left(1000\text{ kg m}^{- 2} \right)v_{A}^{2}\]

or,

\[v_{A} = \sqrt{0 \cdot 4\text{ m}^{2}\text{ s}^{- 2}} = 0 \cdot 63\text{ m s}^{- 1}\]

The rate of flow = (30 cm2) (0 63 m s-1) = 1890 cm3 s-1.
**11.**: _The area of cross section of a large tank is_ 0 5 m2_. It has an opening near the bottom having area of cross section_ 1 cm2_. A load of_ 20 kg _is applied on the water at the top. Find the velocity of the water coming out of the opening at the time when the height of water level is_ 50 cm _above the bottom. Take_ \(g\) = 10 m s-2.

## Questions for short answer

1. Is it always true that the molecules of a dense liquid are heavier than the molecules of a lighter liquid?
2. If someone presses a pointed needle against your skin, you are hurt. But if someone presses a rod against your skin with the same force, you easily tolerate. Explain.
3. In the derivation of \(P_{1} - P_{2} = \varrho gz\), it was assumed that the liquid is incompressible. Why will this equation not be strictly valid for a compressible liquid?
4. Suppose the density of air at Madras is \(r_{0}\) and atmospheric pressure is \(P_{o}\). If we go up, the density and the pressure both decrease. Suppose we wish to calculate the pressure at a height 10 km above Madras. If we use the equation \(P_{0} - P = \varrho_{0}\varrho gz\), will we get a pressure more than the actual or less than the actual? Neglect the variation in \(g\). Does your answer change if you also consider the variation in _g_?
5. The free surface of a liquid resting in an inertial frame is horizontal. Does the normal to the free surface pass through the centre of the earth? Think separately if the liquid is (a) at the equator (b) at a pole (c) somewhere else.
6. A barometer tube reads 76 cm of mercury. If the tube is gradually inclined keeping the open end immersed in the mercury reservoir, will the length of mercury column be 76 cm, more than 76 cm or less than 76 cm?
7. A one meter long glass tube is open at both ends. One end of the tube is dipped into a mercury cup, the tube is kept vertical and the air is pumped out of the tube by connecting the upper end to a suction pump. Can mercury be pulled up into the pump by this process?
8. A satellite revolves round the earth. Air pressure inside the satellite is maintained at 76 cm of mercury. What will be the height of mercury column in a barometer tube 1 m long placed in the satellite?
9. Consider the barometer shown in figure (13-Q1). If a small hole is made at a point \(P\) in the barometer tube, will the mercury come out from this hole?

Figure 13: W7

10. Is Archimedes' principle valid in an elevator accelerating up? In a car accelerating on a level road?
11. Why is it easier to swim in sea water than in fresh water?
12. A glass of water has an ice cube floating in water. The water level just touches the rim of the glass. Will the water overflow when the ice melts?

## Objective

1. A liquid can easily change its shape but a solid can not because (a) the density of a liquid is smaller than that of a solid (b) the forces between the molecules is stronger in solid than in liquids (c) the atoms combine to form bigger molecules in a solid (d) the average separation between the molecules is larger in solids.
2. Consider the equations \[P = \mathop{\mathrm{Lim}}\limits_{\Delta s \to 0}\frac{F}{\Delta S}\text{ and }\,P_{1} - P_{2} = \rho gz.\] In an elevator accelerating upward (a) both the equations are valid (b) the first is valid but not the second (c) the second is valid but not the first (d) both are invalid.
3. The three vessels shown in figure (13-Q2) have same base area. Equal volumes of a liquid are poured in the three vessels. The force on the base will be (a) maximum in vessel \(A\) (b) maximum in vessel \(B\) (c) maximum in vessel \(C\) (d) equal in all the vessels.
4. Equal mass of three liquids are kept in three identical cylindrical vessels \(A\), \(B\) and \(C\). The densities are \(\rho_{\Delta s}\), \(\rho_{\Delta s}\), \(\rho_{C}\) with \(\rho_{A} < \rho_{B} < \rho_{C}\). The force on the base will be (a) maximum in vessel \(A\) (b) maximum in vessel \(B\) (c) maximum in vessel \(C\) (d) equal in all the vessels.
5. Figure (13-Q3) shows a siphon. The liquid shown is water. The pressure difference \(P_{B} - P_{A}\) between the points \(A\) and \(B\) is
13. A ferry boat loaded with rocks has to pass under a bridge. The maximum height of the rocks is slightly more than the height of the bridge so that the boat just fails to pass under the bridge. Should some of the rocks be removed or some more rocks be added?
14. Water is slowly coming out from a vertical pipe. As the water descends after coming out, its area of cross section reduces. Explain this on the basis of the equation of continuity.
15. While watering a distant plant, a gardener partially closes the exit hole of the pipe by putting his finger on it. Explain why this results in the water stream going to a larger distance.
16. A Gipsy car has a canvass top. When the car runs at high speed, the top bulges out. Explain.

the reading will be (a) zero (b) 76 cm (c) \(<76\) cm (d) \(>76\) cm.
10. A barometer kept in an elevator accelerating upward reads 76 cm. The air pressure in the elevator is (a) 76 cm (b) \(<76\) cm (c) \(>76\) cm (d) zero.
11. To construct a barometer, a tube of length 1 m is filled completely with mercury and is inverted in a mercury cup. The barometer reading on a particular day is 76 cm. Suppose a 1 m tube is filled with mercury up to 76 cm and then closed by a cork. It is inverted in a mercury cup and the cork is removed. The height of mercury column in the tube over the surface in the cup will be (a) zero (b) 76 cm (c) \(>76\) cm (d) \(<76\) cm.
12. A 20 N metal block is suspended by a spring balance. A beaker containing some water is placed on a weighing machine which reads 40 N. The spring balance is now lowered so that the block gets immersed in the water. The spring balance now reads 16 N. The reading of the weighing machine will be (a) 36 N (b) 60 N (c) 44 N (d) 56 N.
13. A piece of wood is floating in water kept in a bottle. The bottle is connected to an air pump. Neglect the compressibility of water. When more air is pushed into the bottle from the pump, the piece of wood will float with (a) larger part in the water (b) lesser part in the water (c) same part in the water (d) it will sink.
14. A metal cube is placed in an empty vessel. When water is filled in the vessel so that the cube is completely immersed in the water, the force on the bottom of the vessel in contact with the cube (a) will increase (b) will decrease (c) will remain the same (d) will become zero.
15. A wooden object floats in water kept in a beaker. The object is near a side of the beaker (figure 13-Q4). Let \(P_{1},P_{2},P_{3}\) be the pressures at the three points \(A\), \(B\) and \(C\) of the bottom as shown in the figure. 16. A closed cubical box is completely filled with water and is accelerated horizontally towards right with an acceleration \(a\). The resultant normal force by the water on the top of the box (a) passes through the centre of the top (b) passes through a point to the right of the centre (c) passes through a point to the left of the centre (d) becomes zero.
17. Consider the situation of the previous problem. Let the water push the left wall by a force \(F_{1}\) and the right wall by a force \(F_{2}\). (a) \(F_{1} = F_{2}\) (b) \(F_{1} > F_{2}\) (c) \(F_{1} < F_{2}\) (d) the information is insufficient to know the relation between \(F_{1}\) and \(F_{2}\).
18. Water enters through end \(A\) with a speed \(v_{1}\) and leaves through end \(B\) with a speed \(v_{2}\) of a cylindrical tube \(AB\). The tube is always completely filled with water. In case \(I\) the tube is horizontal, in case \(II\) it is vertical with the end \(A\) upward and in case \(III\) it is vertical with the end \(B\) upward. We have \(v_{1} = v_{2}\) for (a) case \(I\) (b) case \(II\) (c) case \(III\) (d) each case.
19. Bernoulli theorem is based on conservation of (a) momentum (b) mass (c) energy (d) angular momentum.
20. Water is flowing through a long horizontal tube. Let \(P_{A}\) and \(P_{B}\) be the pressures at two points \(A\) and \(B\) of the tube. (a) \(P_{A}\) must be equal to \(P_{B}\). (b) \(P_{A}\) must be greater than \(P_{B}\). (c) \(P_{A}\) must be smaller than \(P_{B}\). (d) \(P_{A} = P_{B}\) only if the cross-sectional area at \(A\) and \(B\) are equal.
21. Water and mercury are filled in two cylindrical vessels up to same height. Both vessels have a hole in the wall near the bottom. The velocity of water and mercury coming out of the holes are \(v_{1}\) and \(v_{2}\) respectively. (a) \(v_{1} = v_{2}\). (b) \(v_{1} = 13 6 \cdot v_{2}\). (c) \(v_{1} = v_{2}/13 6 \cdot v_{2}\). (d) \(P_{2} = P_{3} \cdot P_{1}\).
22. A large cylindrical tank has a hole of area \(A\) at its bottom. Water is poured in the tank by a tube of equal cross-sectional area \(A\) ejecting water at the speed \(v\). (a) The water level in the tank will keep on rising. (b) No water can be stored in the tank (c) The water level will rise to a height \(v^{2}/2\,g\) and then stop. (d) The water level will oscillate.

## Objective ii

(c) The weight of the displaced liquid equals the weight of the solid. (d) The weight of the dipped part of the solid is equal to the weight of the displaced liquid.

Figure 13: Q4

2. The weight of an empty balloon on a spring balance is \(W_{1}\). The weight becomes \(W_{2}\) when the balloon is filled with air. Let the weight of the air itself be \(w\). Neglect the thickness of the balloon when it is filled with air. Also neglect the difference in the densities of air inside and outside the balloon. (a) \(W_{2}=W_{1}\). (b) \(W_{2}=W_{1}+w\). (c) \(W_{2}<W_{1}+w\). (d) \(W_{2}>W_{1}\).
3. A solid is completely immersed in a liquid. The force exerted by the liquid on the solid will (a) increase if it is pushed deeper inside the liquid (b) change if its orientation is changed (c) decrease if it is taken partially out of the liquid (d) be in the vertically upward direction.
4. A closed vessel is half filled with water. There is a hole near the top of the vessel and air is pumped out from this hole. (a) The water level will rise up in the vessel. (b) The pressure at the surface of the water will decrease. (c) The force by the water on the bottom of the vessel will decrease. (d) The density of the liquid will decrease.
5. In a streamline flow, (a) the speed of a particle always remains same (b) the velocity of a particle always remains same (c) the kinetic energies of all the particles arriving at a given point are the same (d) the momenta of all the particles arriving at a given point are the same.
6. Water flows through two identical tubes \(A\) and \(B\). A volume \(V_{\circ}\) of water passes through the tube \(A\) and \(2\,V_{\circ}\) through \(B\) in a given time. Which of the following may be correct? (a) Flow in both the tubes are steady. (b) Flow in both the tubes are turbulent. (c) Flow is steady in \(A\) but turbulent in \(B\). (d) Flow is steady in \(B\) but turbulent in \(A\).
7. Water is flowing in streamline motion through a tube with its axis horizontal. Consider two points \(A\) and \(B\) in the tube at the same horizontal level. (a) The pressures at \(A\) and \(B\) are equal for any shape of the tube. (b) The pressures are never equal. (c) The pressures are equal if the tube has a uniform cross section. (d) The pressures may be equal even if the tube has a nonuniform cross section.
8. There is a small hole near the bottom of an open tank filled with a liquid. The speed of the water ejected does not depend on (a) area of the hole (b) density of the liquid (c) height of the liquid from the hole (d) acceleration due to gravity.

## 10 Exercises

1. The surface of water in a water tank on the top of a house is \(4\,\mathrm{m}\) above the tap level. Find the pressure of water at the tap when the tap is closed. Is it necessary to specify that the tap is closed? Take \(g=10\)\(\mathrm{m}\)\(\mathrm{s}^{-2}\).
2. The heights of mercury surfaces in the two arms of the manometer shown in figure (13-E1) are \(2\) cm and \(8\) cm. Atmospheric pressure \(=1\cdot 01\times 10^{\ 5}\)\(\mathrm{N}\)\(\mathrm{m}^{-2}\). Find (a) the pressure of the gas in the cylinder and (b) the pressure of mercury at the bottom of the U tube.

Figure 13-E1
3. The area of cross section of the wider tube shown in figure (13-E2) is \(900\)\(\mathrm{cm}^{\ 2}\). If the boy standing on the piston weighs \(45\) kg, find the difference in the levels of water in the two tubes.
4. A glass full of water has a bottom of area \(20\)\(\mathrm{cm}^{\ 2}\), top of area \(20\)\(\mathrm{cm}^{\ 2}\), height \(20\)\(\mathrm{cm}\) and volume half a litre. (a) Find the force exerted by the water on the bottom. (b) Considering the equilibrium of the water, find the resultant force exerted by the sides of the glass on the water. Atmospheric pressure \(=1\cdot 0\times 10^{\ 5}\)\(\mathrm{N}\)\(\mathrm{m}^{-2}\). Density of water \(=1000\)\(\mathrm{kg}\)\(\mathrm{m}^{-3}\) and \(g=10\)\(\mathrm{m}\)\(\mathrm{s}^{-2}\). Take all numbers to be exact.
5. Suppose the glass of the previous problem is covered by a jar and the air inside the jar is completely pumped out. (a) What will be the answers to the problem? (b) Show that the answers do not change if a glass of different shape is used provided the height, the bottom area and the volume are unchanged.
6. If water be used to construct a barometer, what would be the height of water column at standard atmospheric pressure (\(76\)\(\mathrm{cm}\) of mercury)?
7. The pressure of the water is \(100\)\(\mathrm{m}\)\(\mathrm{s}^{-2}\). If water is pumped out, the pressure of the water is \(100\)\(\mathrm{m}\)\(\mathrm{s}^{-2}\).

7. Find the force exerted by the water on a 2 m2 plane surface of a large stone placed at the bottom of a sea 500 m deep. Does the force depend on the orientation of the surface?
8. Water is filled in a rectangular tank of size 3 m x 2 m x 1 m. (a) Find the total force exerted by the water on the bottom surface of the tank. (b) Consider a vertical side of area 2 m x 1 m. Take a horizontal strip of width \(\delta\)x metre in this side, situated at a depth of \(x\) metre from the surface of water. Find the force by the water on this strip. (c) Find the torque of the force calculated in part (b) about the bottom edge of this side. (d) Find the total force by the water on this side. (e) Find the total torque by the water on the side about the bottom edge. Neglect the atmospheric pressure and take \(g=10\) m s-2.
9. An ornament weighing 36 g in air, weighs only 34 g in water. Assuming that some copper is mixed with gold to prepare the ornament, find the amount of copper in it. Specific gravity of gold is 19\(\cdot\)3 and that of copper is 8\(\cdot\)9.
10. Refer to the previous problem. Suppose, the goldsmith argues that he has not mixed copper or any other material with gold, rather some cavities might have been left inside the ornament. Calculate the volume of the cavities left that will allow the weights given in that problem.
11. A metal piece of mass 160 g lies in equilibrium inside a glass of water (figure 13-E4). The piece touches the bottom of the glass at a small number of points. If the density of the metal is 8000 kg m-3, find the normal force exerted by the bottom of the glass on the metal piece.
12. A ferry boat has internal volume 1 m-3 and weight 50 kg. (a) Neglecting the thickness of the wood, find the fraction of the volume of the boat immersed in water. (b) If a leak develops in the bottom and water starts coming in, what fraction of the boat's volume will be filled with water before water starts coming in from the sides?
13. A cubical block of ice floating in water has to support a metal piece weighing 0\(\cdot\)5 kg. What can be the minimum edge of the block so that it does not sink in water? Specific gravity of ice = 0\(\cdot\)9.
14. A cube of ice floats partly in water and partly in K.oil (figure 13-E5). Find the ratio of the volume of ice immersed in water to that in K.oil. Specific gravity of K.oil is 0\(\cdot\)8 and that of ice is 0\(\cdot\)9.
15. A cubical box is to be constructed with iron sheets 1 mm in thickness. What can be the minimum value of the external edge so that the cube does not sink in water? Density of iron = 8000 kg m-3 and density of water = 1000 kg m-3.
16. A cubical block of wood weighing 200 g has a lead piece fastened underneath. Find the mass of the lead piece which will just allow the block to float in water. Specific gravity of wood is 0\(\cdot\)8 and that of lead is 11\(\cdot\)3.
17. Solve the previous problem if the lead piece is fastened on the top surface of the block and the block is to float with its upper surface just dipping into water.
18. A cubical metal block of edge 12 cm floats in mercury with one fifth of the height inside the mercury. Water is poured till the surface of the block is just immersed in it. Find the height of the water column to be poured. Specific gravity of mercury = 13\(\cdot\)6.
19. A hollow spherical body of inner and outer radii 6 cm and 8 cm respectively floats half-submerged in water. Find the density of the material of the sphere.
20. A solid sphere of radius 5 cm floats in water. If a maximum load of 0\(\cdot\)1 kg can be put on it without wetting the load, find the specific gravity of the material of the sphere.
21. Find the ratio of the weights, as measured by a spring balance, of a 1 kg block of iron and a 1 kg block of wood. Density of iron = 7800 kg m-3, density of wood = 800 kg m-3 and density of air = 1\(\cdot\)293 kg m-3.
22. A cylindrical object of outer diameter 20 cm and mass 2 kg floats in water with its axis vertical. If it is slightly depressed and then released, find the time period of the resulting simple harmonic motion of the object.
23. A cylindrical object of outer diameter 10 cm, height 20 cm and density 8000 kg m-3 is supported by a vertical spring and is half dipped in water as shown in figure(13-E6). (a) Find the elongation of the spring in equilibrium condition. (b) If the object is slightly depressed and released, find the time period of resulting oscillations of the object. The spring constant = 500 N m-1.

Figure 13: E6

Figure 13: E5

24. A wooden block of mass 0-5 kg and density 800 kg m-3 is fastened to the free end of a vertical spring of spring constant 50 N m-1 fixed at the bottom. If the entire system is completely immersed in water, find (a) the elongation (or compression) of the spring in equilibrium and (b) the time-period of vertical oscillations of the block when it is slightly depressed and released.
25. A cube of ice of edge 4 cm is placed in an empty cylindrical glass of inner diameter 6 cm. Assume that the ice melts uniformly from each side so that it always retains its cubical shape. Remembering that ice is lighter than water, find the length of the edge of the ice cube at the instant it just leaves contact with the bottom of the glass.
26. A U-tube containing a liquid is accelerated horizontally with a constant acceleration _a_p. If the separation between the vertical limbs is \(l\), find the difference in the heights of the liquid in the two arms.
27. At Deoprayag (Garhwal) river Alaknanda mixes with the river Bhagirathi and becomes river Ganga. Suppose Alaknanda has a width of 12 m, Bhagirathi has a width of 8 m and Ganga has a width of 16 m. Assume that the depth of water is same in the three rivers. Let the average speed of water in Alaknanda be 20 km h-1 and in Bhagirathi be 16 km h-1. Find the average speed of water in the river Ganga.
28. Water flows through a horizontal tube of variable cross section (figure 13-E7). The area of cross section at \(A\) and \(B\) are 4 mm2 and 2 mm2 respectively. If 1 cc of water enters per second through \(A\), find (a) the speed of water at \(A\), (b) the speed of water at \(B\) and (c) the pressure difference \(P_{A}\) - \(P_{B}\).
29. Suppose the tube in the previous problem is kept vertical with \(B\) upward. Water enters through \(B\) at the rate of 1 cm3 s-1. Repeat parts (a), (b) and (c). Note that the speed decreases as the water falls down.
30. Water flows through a tube shown in figure (13-E8). The areas of cross section at \(A\) and \(B\) are 1 cm2 and 0-5 cm2 respectively. The height difference between \(A\) and \(B\) is 5 cm. If the speed of water at \(A\) is 10 cm s-1, find (a) the speed at \(B\) and (b) the difference in pressures at \(A\) and \(B\).
31. Water flows through a horizontal tube as shown in figure (13-E9). If the difference of heights of water column in the vertical tubes is 2 cm, and the areas of cross section at \(A\) and \(B\) are 4 cm2 and 2 cm2 respectively, find the rate of flow of water across any section.
32. Water flows through the tube shown in figure (13-E10). The areas of cross section of the wide and the narrow portions of the tube are 5 cm2 and 2 cm2 respectively. The rate of flow of water through the tube is 500 cm3 s-4. Find the difference of mercury levels in the U-tube.
33. Water leaks out from an open tank through a hole of area 2 mm2 in the bottom. Suppose water is filled up to a height of 80 cm and the area of cross section of the tank is 0.4 m2. The pressure at the open surface and at the hole are equal to the atmospheric pressure. Neglect the small velocity of the water near the open surface in the tank. (a) Find the initial speed of water coming out of the hole. (b) Find the speed of water coming out when half of water has leaked out. (c) Find the volume of water leaked out during a time interval _dt_ after the height remained is \(h\). Thus find the decrease in height _dh_ in terms of \(h\) and _dt_. (d) From the result of part (c) find the time required for half of the water to leak out.
34. Water level is maintained in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
35. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
36. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
37. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
38. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
39. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
40. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
41. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
42. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
43. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
44. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
44. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
45. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
46. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
47. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
48. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
49. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
50. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
51. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
52. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
53. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
54. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
55. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
56. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
57. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
58. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
59. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
50. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
51. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
52. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
53. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
54. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
55. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
56. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
57. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
58. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
59. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
51. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
51. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
52. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on a horizontal plane. At what height above the bottom should a hole be made in the vessel so that the water stream coming out of the hole strikes the horizontal plane at the greatest distance from the vessel (figure 13-E11)?
53. Water levels in a cylindrical vessel up to a fixed height \(H\). The vessel is kept on 

## Answers

1. (a), (b), (c) 2. (a), (c) 3. (c), (d) 4. (b), (c) 5. (e), (d) 6. (a), (b), (e) 7. (c), (d) 8. (a), (b) 9. (c) 10000/3 N/m2 12. (a) 120 (b) 19 20 13. 17 cm 14. 1 15. 4 8 cm 16. 54*8 g 17. 50 g 18. 10*4 cm 19. 865 kg m-3 20. 0*8 21. 10015 22. 0*5 s 23. (a) 23*5 cm 24. (a) 25 cm 25. 2*26 cm 26. \(a_{0}\)1/\(g\) 27. 23 km/h 28. (a) 25 cm/s, (b) 50 cm/s 29. (a) 25 cm/s, (b) 50 cm/s, (d) 25 cm/s, (b) 50 cm/s, (c) 188 N/m2 31. (a) 20 cm/s, (b) 485 N/m2 32. 146 cc/s 33. 2*13 cm 34. (a) 4 m/s, (b) \(\sqrt{8}\) m/s 4 (2 mm \({}^{2}\)) \(\sqrt{2\,gh}\)\(dt\), \(\sqrt{2\,gh}\)\(\times 5\times 10^{-6}\)\(dt\) 46. 5 hours 35. \(H\)/2. \(\square\)
