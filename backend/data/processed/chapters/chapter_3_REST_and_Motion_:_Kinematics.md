## Chapter 3 REST and Motion : Kinematics

### 3.1 Rest and Motion

When do we say that a body is at rest and when do we say that it is in motion? You may say that if a body does not change its position as time passes it is at rest. If a body changes its position with time, it is said to be moving. But when do we say that it is not changing its position? A book placed on the table remains on the table and we say that the book is at rest. However, if we station ourselves on the moon (the Apollo missions have made it possible), the whole earth is found to be changing its position and so the room, the table and the book are all continuously changing their positions. The book is at rest if it is viewed from the room, it is moving if it is viewed from the moon.

Motion is a combined property of the object under study and the observer. There is no meaning of rest or motion without the viewer. Nothing is in absolute rest or in absolute motion. The moon is moving with respect to the book and the book moves with respect to the moon. Take another example. A robber enters a train moving at great speed with respect to the ground, brings out his pistol and says "Don't move, stand still". The passengers stand still. The passengers are at rest with respect to the robber but are moving with respect to the rail track.

To locate the position of a particle we need a _frame of reference_. A convenient way to fix up the frame of reference is to choose three mutually perpendicular axes and name them _X-Y-Z_ axes. The coordinates, (x, y, z) of the particle then specify the position of the particle with respect to that frame. Add a clock into the frame of reference to measure the time. If all the three coordinates _x, y_ and \(z\) of the particle remain unchanged as time passes, we say that the particle is at rest with respect to this frame. If any one or more coordinates change with time, we say that the body is moving with respect to this frame.

There is no rule or restriction on the choice of a frame. We can choose a frame of reference according to our convenience to describe the situation under study. Thus, when we are in a train it is convenient to choose a frame attached to our compartment. The coordinates of a suitcase placed on the upper berth do not change with time (unless the train gives a jerk) and we say that the suitcase is at rest in the train-frame. The different stations, electric poles, trees etc. change their coordinates and we say that they are moving in the train-frame. Thus, we say that "Bombay is coming" and "Pune has already passed".

In the following sections we shall assume that the frame of reference is already chosen and we are describing the motion of the objects in the chosen frame. Sometimes the choice of the frame is clear from the context and we do not mention it. Thus, when one says the car is travelling and the rickshaw is not, it is clear that all positions are measured from a frame attached to the road.

### 3.2 Distance and Displacement

Suppose a particle is at \(A\) at time \(t_{1}\) and at \(B\) at time \(t_{2}\) with respect to a given frame (figure 3.2).

Figure 3.2

Figure 3.1During the time interval \(t_{1}\) to \(t_{2}\) the particle moves along the path ACB. The length of the path ACB is called the _distance_ travelled during the time interval \(t_{1}\) to \(t_{2}\). If we connect the initial position \(A\) with the final position \(B\) by a straight line, we get the _displacement_ of the particle. The magnitude of the displacement is the length of the straight line joining the initial and the final position. The direction is from the initial to the final position. The displacement has both the magnitude as well as the direction. Further the displacements add according to the triangle rule of vector addition. Suppose a particle kept on a table is displaced on the table and at the same time the table is also displaced in the room. The net displacement of the particle in the room is obtained by the vector sum of the two displacements. Thus, displacement is a vector quantity. In contrast the distance covered has only a magnitude and is thus, a scalar quantity.

**Example 3.1**:

_An old person moves on a semi-circular track of radius \(40\,\mathrm{\SIUnitSymbolOhm}\) during a morning walk. If he starts at one end of the track and reaches at the other end, find the distance covered and the displacement of the person._
**Solution**: _The distance covered by the person equals the length of the track. It is equal to_ \(\pi R=\pi\times 40\,\mathrm{\SIUnitSymbolOhm}\) _m =_ \(126\,\mathrm{m}\)_._

_The displacement is equal to the diameter of the semi-circular track joining the two ends. It is_ \(2\,R=2\times 40\,\mathrm{\SIUnitSymbolOhm}\) _m =_ \(80\,\mathrm{m}\)_. The direction of this displacement is from the initial point to the final point._

### Average speed and instantaneous speed

The average speed of a particle in a time interval is defined as the distance travelled by the particle divided by the time interval. If the particle travels a distance \(s\) in time \(t_{1}\) to \(t_{2}\), the _average speed_ is defined as

\[v_{av}=\frac{s}{t_{2}-t_{1}}\,. \tag{3.1}\]

The average speed gives the overall "rapidity" with which the particle moves in this interval. In a one-day cricket match, the average run rate is quoted as the total runs divided by the total number of overs used to make these runs. Some of the overs may be expensive and some may be economical. Similarly, the average speed gives the total effect in the given interval. The rapidity or slowness may vary from instant to instant. When an athelete starts running, he or she runs slowly and gradually increases the rate. We define the _instantaneous speed_ at a time \(t\) as follows.

Let \(\Delta s\) be the distance travelled in the time interval \(t\) to \(t+\Delta t\). The average speed in this time interval is

\[v_{av}=\frac{\Delta s}{\Delta t}\,.\]

Now make \(\Delta t\) vanishingly small and look for the value of \(\frac{\Delta s}{\Delta t}\). Remember \(\Delta s\) is the distance travelled in the chosen time interval \(\Delta t\). As \(\Delta t\) approaches \(0\), the distance \(\Delta s\) also approaches zero but the ratio \(\frac{\Delta s}{\Delta t}\) has a finite limit.

The instantaneous speed at a time \(t\) is defined as

\[v=\lim_{\Delta t\to 0}\frac{\Delta s}{\Delta t}=\frac{ds}{dt}\, \tag{3.2}\]

where \(s\) is the distance travelled in time \(t\). The average speed is defined for a time interval and the instantaneous speed is defined at a particular instant. Instantaneous speed is also called "speed".

**Example 3.2**:

_The distance travelled by a particle in time t is given by \(s=(2\cdot 5\,\mathrm{m/s}^{\ 2})\,t^{\ 2}\). Find (a) the average speed of the particle during the time \(0\) to \(5\cdot 0\,\mathrm{s}\), and (b) the instantaneous speed at \(t=5\cdot 0\,\mathrm{s}\)._
**Solution**: _(a) The distance travelled during time \(0\) to \(5\cdot 0\,\mathrm{s}\) is_

\[s=(2\cdot 5\,\mathrm{m/s}^{\ 2})\,(5\cdot 0\,\mathrm{s})^{\ 2}=62\cdot 5\,\mathrm{m}.\]

_The average speed during this time is_

\[v_{av}=\frac{62\cdot 5\,\mathrm{m}}{5\,\mathrm{s}}=12\cdot 5\,\mathrm{m/s}.\]
**(b)**: \(s=(2\cdot 5\,\mathrm{m/s}^{\ 2})\,t^{\ 2}\)__
**or,**: \(\frac{ds}{dt}=(2\cdot 5\,\mathrm{m/s}^{\ 2})\,(2\,t)=(5\cdot 0\,\mathrm{m/s}^{\ 2})\,t\)_._

_At_ \(t=5\cdot 0\,\mathrm{s}\) _the speed is_

\[v=\frac{ds}{dt}=(5\cdot 0\,\mathrm{m/s}^{\ 2})\,(5\cdot 0\,\mathrm{s})=25\, \mathrm{m/s}.\]

If we plot the distance \(s\) as a function of time (figure 3.4), the speed at a time \(t\) equals the slope of

Figure 3.3

the tangent to the curve at the time \(t\). The average speed in a time interval \(t\) to \(t+\Delta t\) equals the slope of the chord \(AB\) where \(A\) and \(B\) are the points on the curve corresponding to the time \(t\) and \(t+\Delta t\). As \(\Delta t\) approaches zero, the chord \(AB\) becomes the tangent at \(A\) and the average speed \(\frac{\Delta s}{\Delta t}\) becomes the slope of the tangent which is \(\frac{ds}{dt}\).

If the speed of the particle at time \(t\) is \(v\), the distance \(ds\) travelled by it in the short time interval \(t\) to \(t+dt\) is \(v\)\(dt\). Thus, \(ds=vdt\). The total distance travelled by the particle in a finite time interval \(t_{1}\) to \(t_{2}\) can be obtained by summing over these small distances \(ds\) as time changes from \(t_{1}\) to \(t_{2}\). Thus, the distance travelled by a particle in the time interval \(t_{1}\) to \(t_{2}\) is

\[s=\int_{t_{1}}^{t_{2}}v\;dt. \tag{3.3}\]

If we plot a graph of the speed \(v\) versus time \(t\), the distance travelled by the particle can be obtained by finding the area under the curve. Figure (3.5) shows such a speed-time graph. To find the distance travelled in the time interval \(t_{1}\) to \(t_{2}\) we draw ordinates from \(t+t_{1}\) and \(t=t_{2}\). The area bounded by the curve \(v-t\), the \(X\)-axis and the two ordinates at \(t=t_{1}\) and \(t=t_{2}\) (shown shaded in the figure) gives the total distance covered.

The dimension of speed is \(\text{LT}^{-1}\) and its SI unit is metre/second abbreviated as m/s.

**Example 3.3**:

_Figure (3.6) shows the speed versus time graph for a particle. Find the distance travelled by the particle during the time \(t=0\) to \(t=3\) s._

_Solution :_ The distance travelled by the particle in the time \(0\) to \(3\) s is equal to the area shaded in the figure. This is a right angled triangle with height = \(6\) m/s and the base = \(3\) s. The area is \(\frac{1}{2}\,(\text{base})\,(\text{height})=\frac{1}{2}\times\,(3\) s) \((6\,\text{m/s})=9\,\text{m}\). Thus, the particle covered a distance of \(9\) m during the time \(0\) to \(3\) s.

### Average velocity and instantaneous velocity

The _average velocity_ of a particle in a time interval \(t_{1}\) to \(t_{2}\) is defined as its displacement divided by the time interval. If the particle is at a point \(A\) (figure 3.7) at time \(t=t_{1}\) and at \(B\) at time \(t=t_{2}\), the displacement in this time interval is the vector \(\overrightarrow{AB}\). The average velocity in this time interval is then,

\[\overrightarrow{v_{av}}=\frac{\overrightarrow{AB}}{t_{2}-t_{1}}.\]

Like displacement, it is a vector quantity.

**Position vector :** If we join the origin to the position of the particle by a straight line and put an arrow towards the position of the particle, we get the _position vector_ of the particle. Thus, the position vector of the particle shown in figure (3.7) at time \(t=t_{1}\) is \(\overrightarrow{OA}\) and that at \(t=t_{2}\) is \(\overrightarrow{OB}\). The displacement of the particle in the time interval \(t_{1}\) to \(t_{2}\) is

Figure 3.7:

Figure 3.6:

Figure 3.4:

The average velocity of a particle in the time interval \(t_{1}\) to \(t_{2}\) can be written as

\[\overset{\rightarrow}{v}_{av}^{\rightarrow}=\frac{\overset{\rightarrow}{r_{2}-r_ {1}}}{t_{2}-t_{1}}\,.\hskip 56.905512pt... \tag{3.4}\]

Note that only the positions of the particle at time \(t=t_{1}\) and \(t=t_{2}\) are used in calculating the average velocity. The positions in between \(t_{1}\) and \(t_{2}\) are not needed, hence the actual path taken in going from \(A\) to \(B\) is not important in calculating the average velocity.

**Example 3.4**: \(\hskip 56.905512pt\)__

_A table clock has its minute hand 4_\(\cdot\)0 cm _long. Find the average velocity of the tip of the minute hand (a) between 6\(\cdot\)00 a.m. to 6\(\cdot\)30 a.m. and (b) between 6\(\cdot\)00 a.m. to 6\(\cdot\)30 p.m._
**Solution :**: At 6\(\cdot\)00 a.m. the tip of the minute hand is at 12 mark and at 6\(\cdot\)30 a.m. or 6\(\cdot\)30 p.m. it is 180\({}^{\circ}\) away. Thus, the straight line distance between the initial and final position of the tip is equal to the diameter of the clock.

Displacement = 2 \(R\) = 2 \(\times\) 4\(\cdot\)0 cm = 8\(\cdot\)0 cm.

The displacement is from the 12 mark to the 6 mark on the clock panel. This is also the direction of the average velocity in both cases.

(a) The time taken from 6\(\cdot\)00 a.m. to 6\(\cdot\)30 a.m. is 30 minutes = 1800 s. The average velocity is

\[v_{av}=\frac{\text{Displacement}}{\text{time}}=\frac{8\cdot\text{0 cm}}{1800 \text{ s}}=4\cdot 4\times 10^{-3}\,\text{cm/s}.\]

(b) The time taken from 6\(\cdot\)00 a.m. to 6\(\cdot\)30 p.m. is 12 hours and 30 minutes = 45000 s. The average velocity is

\[v_{av}=\frac{\text{Displacement}}{\text{time}}=\frac{8\cdot\text{0 cm}}{45000 \text{ s}}=1\cdot 8\times 10^{-4}\,\text{cm/s}.\]

The _instantaneous velocity_ of a particle at a time \(t\) is defined as follows. Let the average velocity of the particle in a short time interval \(t\) to \(t\) + \(\Delta t\) be \(\overset{\rightarrow}{v}_{av}\). This average velocity can be written as

\[\overset{\rightarrow}{v}_{av}^{\rightarrow}=\frac{\overset{\rightarrow}{ \Delta r}}{\Delta t}\]

where \(\overset{\rightarrow}{\Delta r}\) is the displacement in the time interval \(\Delta t\). We now make \(\Delta t\) vanishingly small and find the limiting value of \(\frac{\overset{\rightarrow}{\Delta r}}{\Delta t}\). This value is instantaneous velocity \(\overset{\rightarrow}{v}\) of the particle at time \(t\).

\[\overset{\rightarrow}{v}=\lim_{\Delta t\to 0}\frac{\overset{\rightarrow}{\Delta r}}{\Delta t}=\frac{d\overset{\rightarrow}{r}}{dt}.\hskip 56.905512pt... \tag{3.5}\]

For very small intervals the displacement \(\overset{\rightarrow}{\Delta r}\) is along the line of motion of the particle. Thus, the length \(\Delta r\) equals the distance \(As\) travelled in that interval. So the magnitude of the velocity is

\[v=\left|\frac{d\overset{\rightarrow}{r}}{dt}\right|=\frac{1d\overset{ \rightarrow}{r}}{dt}=\frac{ds}{dt}\hskip 56.905512pt... \tag{3.6}\]

which is the instantaneous speed at time \(t\). Instantaneous velocity is also called the "velocity".

### Average Acceleration and Instantaneous Acceleration

If the velocity of a particle remains constant as time passes, we say that it is moving with uniform velocity. If the velocity changes with time, it is said to be accelerated. The acceleration is the rate of change of velocity. Velocity is a vector quantity hence a change in its magnitude or direction or both will change the velocity.

Suppose the velocity of a particle at time \(t_{1}\) is \(\overset{\rightarrow}{v}_{1}\) and at time \(t_{2}\) it is \(\overset{\rightarrow}{v}_{2}\). The change produced in time interval \(t_{1}\) to \(t_{2}\) is \(\overset{\rightarrow}{v}_{2}\)\(\overset{\rightarrow}{-v}_{1}\). We define the _average acceleration_\(\overset{\rightarrow}{a}_{av}\) as the change in velocity divided by the time interval. Thus,

\[\overset{\rightarrow}{a}_{av}^{\rightarrow}=\frac{\overset{\rightarrow}{v}_{2} \overset{\rightarrow}{-v}_{1}}{t_{2}-t_{1}}\,.\hskip 56.905512pt... \tag{3.7}\]

Again the average acceleration depends only on the velocities at time \(t_{1}\) and \(t_{2}\). How the velocity changed in between \(t_{1}\) and \(t_{2}\) is not important in defining the average acceleration.

_Instantaneous acceleration_ of a particle at time \(t\) is defined as

\[\overset{\rightarrow}{a}=\lim_{\Delta t\to 0}\frac{\overset{\rightarrow}{\Delta v}}{\Delta t}=\frac{d\overset{\rightarrow}{v}}{dt}\hskip 56.905512pt... \tag{3.8}\]

where \(\overset{\rightarrow}{\Delta v}\) is the change in velocity between the time \(t\) and \(t\) + \(\Delta t\). At time \(t\) the velocity is \(\overset{\rightarrow}{v}\) and at time \(t+\Delta t\) it becomes \(\overset{\rightarrow}{v}+\Delta v\). \(\overset{\rightarrow}{\Delta v}\) is the average acceleration of the particle in the interval \(\Delta t\). As \(\Delta t\) approaches zero, this average acceleration becomes the instantaneous acceleration. Instantaneous acceleration is also called _"acceleration"_.

The dimension of acceleration is LT\({}^{-2}\) and its SI unit is metre/second\({}^{2}\) abbreviated as m/s\({}^{2}\).

### Motion in a Straight Line

When a particle is constrained to move on a straight line, the description becomes fairly simple. We choose the line as the \(X\)-axis and a suitable time instant as \(t=0\). Generally the origin is taken at the point where the particle is situated at \(t=0\). The position of the particle at time \(t\) is given by its coordinate \(x\) at that time. The velocity is \[v=\frac{dx}{dt}... \tag{3.9}\]

and the acceleration is \(a=\frac{dv}{dt}\)... (3.10)

\[=\frac{d}{dt}\Bigg{(}\frac{dx}{dt}\Bigg{)}=\frac{d^{\ 3}x}{dt^{\ 2}}\.\ \ \ \... \tag{3.11}\]

If \(\frac{dx}{dt}\) is positive, the direction of the velocity is along the positive _X_-axis and if \(\frac{dx}{dt}\) is negative, the direction, is along the negative _X_-axis. Similarly if \(\frac{dv}{dt}\) is positive, the acceleration is along the positive _X_-axis and if \(\frac{dv}{dt}\) is negative, the acceleration is along the negative _X_-axis. The magnitude of \(v\) is speed. If the velocity and the acceleration are both positive, the speed increases. If both of them are negative then also the speed increases but if they have opposite signs, the speed decreases. When the speed decreases, we say that the particle is decelerating. Deceleration is equivalent to negative acceleration. An acceleration of \(2\cdot 0\ \text{m/s}^{\ 2}\) towards east is same as a deceleration of \(2\cdot 0\ \text{m/s}^{\ 2}\) towards west.

### Motion with Constant Acceleration

Suppose the acceleration of a particle is \(a\) and remains constant. Let the velocity at time \(0\) be \(u\) and the velocity at time \(t\) be \(v\). Thus,

\[\frac{dv}{dt}=a,\ \ \ \text{or},\ \ \ \ dv=a\ dt\]

or, \(\int\limits_{u}^{v}dv=\int\limits_{0}^{t}a\ dt.\)

As time changes from \(0\) to \(t\) the velocity changes from \(u\) to \(v\). So on the left hand side the summation is made over \(v\) from \(u\) to \(v\) whereas on the right hand side the summation is made on time from \(0\) to \(t\). Evaluating the integrals, we get,

\[[v]_{u}^{v}=a[t]_{0}^{t}\]

or, \(v-u=at\)

or, \(v=u+at\).

Equation (3.12) may be written as

\[\frac{dx}{dt}=u+at\]

or, \(dx=(u+at)dt\)

or, \(\int\limits_{0}^{x}dx=\int\limits_{0}^{t}(u+at)dt.\)

At \(t=0\) the particle is at \(x=0\). As time changes from \(0\) to \(t\) the position changes from \(0\) to \(x\). So on the left hand side the summation is made on position from \(0\) to \(x\) whereas on the right hand side the summation is made on time from \(0\) to \(t\). Evaluating the integrals, the above equation becomes

\[[x]_{0}^{x}=\int\limits_{0}^{t}u\ dt+\int\limits_{0}^{t}at\ dt\]

or, \(x=u\int\limits_{0}^{t}dt+a\int\limits_{0}^{t}dt\)

\[=u[t]_{0}^{t}+a\bigg{[}\frac{t}{2}\bigg{]}_{0}^{t}\]

or, \(x=ut+\frac{1}{2}\ at^{\ 2}\).... (3.13)

From equation (3.12),

\[v^{\ 2}=(u+at)^{\ 2}\]

or, \(=u^{\ 2}+2\ uat+a^{\ 2}t^{\ 2}\)

or, \(=u^{\ 2}+2a\bigg{(}ut+\frac{1}{2}\ at^{\ 2}\bigg{)}\)

or, \(=u^{\ 2}+2ax\).... (3.14)

The three equations (3.12) to (3.14) are collected below in table 3.1. They are very useful in solving the problems of motion in a straight line with constant acceleration.

Remember that \(x\) represents the position of the particle at time \(t\) and not (in general) the distance travelled by it in time \(0\) to \(t\). For example, if the particle starts from the origin and goes upto \(x=4\ \text{m}\), then turns and is at \(x=2\ \text{m}\) at time \(t\), the distance travelled is \(6\ \text{m}\) but the position is still given by \(x=2\ \text{m}\).

The quantities \(u\), \(v\) and \(a\) may take positive or negative values depending on whether they are directed along the positive or negative direction. Similarly \(x\) may be positive or negative.

**Example 3.6**: _A particle having initial velocity \(u\) moves with a constant acceleration \(a\) for a time \(t\). (a) Find the displacement of the particle in the last \(1\) second. (b) Evaluate it for \(u=5\) m/s, \(a=2\) m/s\({}^{2}\) and \(t=10\) s._
**Solution :**: (a) The position at time \(t\) is

\[s=ut+\frac{1}{2}at^{\ 2}\]

The position at time (\(t-1\) s) is

\[s^{\prime}=u(t-1\) s)+\frac{1}{2}a(t-1\) s)\({}^{2}\]

\[=ut-u(1\) s)+\frac{1}{2}at^{\ 2}-at(1\) s)+\frac{1}{2}a(1\) s)\({}^{2}\]

Thus, the displacement in the last \(1\) s is

\[s_{t}=s-s^{\prime}\]

\[=u(1\) s)+at(1\) s)-\frac{1}{2}a(1\) s)\({}^{2}\]

or, \[s_{t}=u(1\) s)+\frac{a}{2}(2\,t-1\) s)(1 s).... (i)
**(b) Putting the given values in (i)**

\[s_{t}=\] \[= 5\;\text{m}+\left(1\;\frac{\text{m}}{\text{s}^{\frac{1}{2}}} \right)(19\;\text{s})(1\;\text{s})\] \[= 5\;\text{m}+19\;\text{m}=24\;\text{m}.\]

Sometimes, we are not careful in writing the units appearing with the numerical values of physical quantities. If we forget to write the unit of second in equation (i), we get,

\[s_{t}=u+\frac{a}{2}(2\,t-1).\]

This equation is often used to calculate the displacement in the "\(t\)th second". However, as you can verify, different terms in this equation have different dimensions and hence the above equation is dimensionally incorrect. Equation (i) is the correct form which was used to solve part (b).

Also note that this equation gives the displacement of the particle in the last \(1\) second and not necessarily the distance covered in that second.

## Freely Falling Bodies

A common example of motion in a straight line with constant acceleration is free fall of a body near the earth's surface. If air resistance is neglected and a body is dropped near the surface of the earth, it falls along a vertical straight line. The acceleration is in the vertically downward direction and its magnitude is almost constant if the height is small as compared with the radius of the earth (6400 km). This magnitude is approximately equal to 9\(\cdot\)8 m/s\({}^{2}\) or 32 ft/s\({}^{2}\) and is denoted by the letter \(g\).

If we take vertically upward as the positive \(Y\)-axis, acceleration is along the negative \(Y\)-axis and we write \(a=-g\). The equation (3.12) to (3.14) may be written in this case as

\[v=u-gt\]

\[y=ut-\frac{1}{2}gt^{\ 2}\]

\[v^{\ 2}=u^{\ 2}-2\text{g}y.\]

Here \(y\) is the \(y\)-coordinate (that is the height above the origin) at time \(t\), \(u\) is the velocity in \(y\) direction at \(t=0\) and \(v\) is the velocity in \(y\) direction at time \(t\). The position of the particle at \(t=0\) is \(y=0\).

Sometimes it is convenient to choose vertically downward as the positive \(Y\)-axis. Then \(a=g\) and the equations (3.12) to (3.14) become

\[v=u+gt\]

\[y=ut+\frac{1}{2}gt^{\ 2}\]

\[v^{\ 2}=u^{\ 2}+2\text{g}y.\]

**Example 3.7**: _A ball is thrown up at a speed of 4\(\cdot\)0 m/s. Find the maximum height reached by the ball. Take \(g=10\) m/s\({}^{2}\)._
**Solution :**: Let us take vertically upward direction as the positive \(Y\)-axis. We have \(u=4\cdot 0\) m/s and \(a=-10\) m/s\({}^{2}\). At the highest point the velocity becomes zero. Using the formula,\[v^{\ 2}=u^{\ 2}+2ay,\] \[0=(4\,0\ {\rm m/s}^{\ 2}+2(-10\ {\rm m/s}^{\ 2}y\] \[{\rm or},\qquad y=\frac{16\ {\rm m}^{\ 2}/{\rm s}^{\ 2}}{20\ { \rm m/s}^{\ 2}}=0\cdot 80\ {\rm m}.\]

### Motion in a plane

If a particle is free to move in a plane, its position can be located with two coordinates. We choose the plane of motion as the \(X\)-\(Y\) plane. We choose a suitable instant as \(t=0\) and choose the origin at the place where the particle is situated at \(t=0\). Any two convenient mutually perpendicular directions in the \(X\)-\(Y\) plane are chosen as the \(X\) and \(Y\)-axes.

The position of the particle at a time \(t\) is completely specified by its coordinates \((x,y)\). The coordinates at time \(t+\Delta t\) are \((x+\Delta x,y+\Delta y)\). Figure (3.8) shows the positions at \(t\) and \(t+\Delta t\) as \(A\) and \(B\) respectively. The displacement during the time interval \(t\) to \(t+\Delta t\) is

\[\begin{array}{l}\Delta\overrightarrow{x}=\overrightarrow{AB}=\overrightarrow{AC}+C \overrightarrow{B}\\ =\Delta x\overrightarrow{i}+\Delta y\overrightarrow{j}\\ \Delta t=\overrightarrow{\Delta x}-\overrightarrow{i}+\frac{\Delta y}{\Delta t }\overrightarrow{j}.\end{array}\]

Taking limits as \(\Delta t\to 0\)

\[\overrightarrow{v}=\frac{dx}{dt}\overrightarrow{i}+\frac{dy}{dt} \overrightarrow{j}.\qquad\qquad\qquad... \tag{3.15}\]

Thus, we see that the \(x\)-component of the velocity is

\[v_{x}=\frac{dx}{dt}\qquad\qquad\qquad... \tag{3.16}\]

and the \(y\)-component is

\[v_{y}=\frac{dy}{dt}.\qquad\qquad\qquad... \tag{3.17}\]

Differentiating (3.15) with respect to time,

\[\overrightarrow{a}=\frac{d\overrightarrow{v}}{dt}=\frac{dv_{x}}{dt} \overrightarrow{i}+\frac{dv_{y}}{dt}\overrightarrow{j}\]

Thus, the acceleration has components

\[a_{x}=\frac{dv_{x}}{dt}\qquad\qquad\qquad... \tag{3.18}\]

and

\[a_{y}=\frac{dv_{y}}{dt}\,.\qquad\qquad\qquad... \tag{3.19}\]

We see that the \(x\)-coordinate, the \(x\)-component of velocity \(v_{x}\) and the \(x\)-component of acceleration \(a_{x}\) are related by

\[v_{x}=\frac{dx}{dt}\quad\mbox{and}\quad a_{x}=\frac{dv_{x}}{dt}\,.\]

These equations are identical to equations (3.9) and (3.10). Thus, if \(a_{x}\) is constant, integrating these equations we get

\[\left.\begin{array}{l}v_{x}=u_{x}+a_{x}\,t\\ x=u_{x}t+\frac{1}{2}\,a_{x}t^{\ 2}\\ v_{x}^{\ 2}=u_{x}^{\ 2}+2a_{x}x\end{array}\right|\qquad\qquad... \tag{3.20}\]

where \(u_{x}\) is the \(x\)-component of the velocity at \(t=0\). Similarly we have

\[v_{y}=\frac{dy}{dt}\quad\mbox{and}\quad a_{y}=\frac{dv_{y}}{dt}\]

and if \(a_{y}\) is constant,

\[\left.\begin{array}{l}v_{y}=u_{y}+a_{y}t\\ y=u_{y}t+\frac{1}{2}\,a_{y}t^{\ 2}\\ v_{y}^{\ 2}=u_{y}^{\ 2}+2a_{y}y\end{array}\right|\qquad\qquad... \tag{3.21}\]

The general scheme for the discussion of motion in a plane is therefore simple. The \(x\)-coordinate, the \(x\)-component of velocity and the \(x\)-component of acceleration are related by equations of straight line motion along the \(X\)-axis. Similarly the \(y\)-coordinate, the \(y\)-component of velocity and the \(y\)-component of acceleration are related by the equations of straight line motion along the \(Y\)-axis. The problem of motion in a plane is thus, broken up into two independent problems of straight line motion, one along the \(X\)-axis and the other along the \(Y\)-axis.

**Solution**: : \(a_{x}=(1\cdot 5\) m/s \({}^{2})\) (cos37\({}^{\circ}\))

\[=(1\cdot 5\) m/s \({}^{2})\times\frac{4}{5}=1\cdot 2\) m/s \({}^{2}\]

and \(a_{y}=(1\cdot 5\) m/s \({}^{2})\) (sin37\({}^{\circ}\))

\[=(1\cdot 5\) m/s \({}^{2})\times\frac{3}{5}=0\cdot 90\) m/s \({}^{2}\).

The initial velocity has components

\[u_{x}=8\cdot 0\]

m/s

and \(u_{y}=0\)

At \(t=0\), \(x=0\) and \(y=0\).

The \(x\)-component of the velocity at time \(t=4\cdot 0\) s is given by

\[v_{x}=u_{x}+a_{y}t\]

\[=8\cdot 0\]

m/s \({}^{2}\) (4\cdot 0\) s)

\[=8\cdot 0\]

m/s \({}^{2}\) (8\cdot 0\) m/s \({}^{2}\) (8\cdot 0\) m/s \({}^{2}\)

The \(y\)-component of velocity at \(t=4\cdot 0\) s is given by

\[v_{y}=u_{y}+a_{y}t\]

\[=0+(0\cdot 90\]

m/s \({}^{2})\) (4\cdot 0\) s) = 3\(\cdot 6\) m/s.

The velocity of the particle at \(t=4\cdot 0\) s is

\[v=\sqrt{v_{x}^{2}+v_{y}^{2}}=\sqrt{(12\cdot 8\]

m/s) \({}^{2}+(3\cdot 6\) m/s) \({}^{2}}\)

\[=13\cdot 3\]

m/s.

The velocity makes an angle \(\theta\) with the \(X\)-axis where

\[\tan\theta=\frac{v_{y}}{v_{x}}=\frac{3\cdot 6\ \mbox{m/s}}{12\cdot 8\ \mbox{m/s}}= \frac{9}{32}\cdot\]

The \(x\)-coordinate at \(t=4\cdot 0\) s is

\[x=u_{x}t+\frac{1}{2}a_{x}t^{2}\]

\[=(8\cdot 0\ \mbox{m/s})\,(4\cdot 0\ \mbox{s})+\frac{1}{2}(1\cdot 2\ \mbox{m/s}^{2}) (4\cdot 0\ \mbox{s})^{2}\]

\[=32\ \mbox{m}+9\cdot 6\ \mbox{m}=41\cdot 6\ \mbox{m}.\]

The \(y\)-coordinate at \(t=4\cdot 0\) s is

\[y=u_{y}t+\frac{1}{2}a_{y}t^{2}\]

\[=\frac{1}{2}(0\cdot 90\ \mbox{m/s}^{2})\,(4\cdot 0\ \mbox{s})^{2}\]

\[=7\cdot 2\ \mbox{m}.\]

Thus, the particle is at (41\(\cdot\)6 m, 7\(\cdot\)2 m) at 4\(\cdot 0\) s.

### Projectile Motion

An important example of motion in a plane with constant acceleration is the projectile motion. When a particle is thrown obliquely near the earth's surface, it moves along a curved path. Such a particle is called a _projectile_ and its motion is called _projectile motion_. We shall assume that the particle remains close to the surface of the earth and the air resistance is negligible. The acceleration of the particle is then almost constant. It is in the vertically downward direction and its magnitude is \(g\) which is about 9\(\cdot\)8 m/s \({}^{2}\).

Let us first make ourselves familiar with certain terms used in discussing projectile motion. Figure (3.10) shows a particle projected from the point \(O\) with an initial velocity \(u\) at an angle \(\theta\) with the horizontal. It goes through the highest point \(A\) and falls at \(B\) on the horizontal surface through \(O\). The point \(O\) is called the _point of projection_, the angle \(\theta\) is called the _angle of projection_ and the distance \(OB\) is called the _horizontal range_ or simply _range_. The total time taken by the particle in describing the path \(OAB\) is called the _time of flight_.

The motion of the projectile can be discussed separately for the horizontal and vertical parts. We take the origin at the point of projection.

The instant when the particle is projected is taken as \(t=0\). The plane of motion is taken as the \(X\)-\(Y\) plane. The horizontal line \(OX\) is taken as the \(X\)-axis and the vertical line \(OY\) as the \(Y\)-axis. Vertically upward direction is taken as the positive direction of the \(Y\)-axis.

We have \(u_{x}=u\ \mbox{cos}\theta\) ; \(a_{x}=0\)

\(u_{y}=u\ \mbox{sin}\theta\) ; \(a_{y}=-g\).

**Horizontal Motion**: As \(a_{x}=0\), we have

\[v_{x}=u_{x}+a_{x}t=u_{x}=u\ \mbox{cos}\theta\]

and \(x=u_{x}t+\frac{1}{2}a_{x}t^{2}=u_{x}t=ut\ \mbox{cos}\theta\).

As indicated in figure (3.10), the \(x\)-component of the velocity remains constant as the particle moves.

### Vertical Motion

The acceleration of the particle is \(g\) in the downward direction. Thus, \(a_{y}=-g\). The \(y\)-component of the initial velocity is \(u_{y}\). Thus,

\[v_{y}=u_{y}-gt\]

and \(y=u_{y}t-\frac{1}{2}gt^{2}\).

Also we have,

\[v_{y}^{2}=u_{y}^{2}-2g\mbox{y}.\]

Figure 3.10:The vertical motion is identical to the motion of a particle projected vertically upward with speed \(u\) sin\(\theta\). The horizontal motion of the particle is identical to a particle moving horizontally with uniform velocity \(u\) cos\(\theta\).

#### Time of Flight

Consider the situation shown in figure (3.10). The particle is projected from the point \(O\) and reaches the same horizontal plane at the point \(B\). The total time taken to reach \(B\) is the time of flight.

Suppose the particle is at \(B\) at a time \(t\). The equation for horizontal motion gives

\[OB=x=ut\ \mbox{cos}\theta\]

The \(y\)-coordinate at the point \(B\) is zero. Thus, from the equation of vertical motion,

\[y=ut\ \mbox{sin}\theta-\frac{1}{2}\,gt^{\ 2}\]

\[\mbox{or,}\hskip 56.905512pt0=ut\ \mbox{sin}\theta-\frac{1}{2}\,gt^{\ 2}\]

\[\mbox{or,}\hskip 56.905512ptt(u\ \mbox{sin}\theta-\frac{1}{2}\,gt)=0.\]

Thus, either \(t=0\) or, \(t=\frac{2u\ \mbox{sin}\theta}{g}\).

Now \(t=0\) corresponds to the position \(O\) of the particle. The time at which it reaches \(B\) is thus,

\[T=\frac{2u\ \mbox{sin}\theta}{g}\,.\hskip 56.905512pt... \tag{3.22}\]

This is the time of flight.

#### Range

The distance \(OB\) is the horizontal range. It is the distance travelled by the particle in time \(T=\frac{2u\ \mbox{sin}\theta}{g}\). By the equation of horizontal motion,

\[x=(u\mbox{cos}\theta)t\]

\[\mbox{or,}\hskip 28.452756ptOB=(u\ \mbox{cos}\theta)\left(\frac{2u\ \mbox{sin}\theta}{g}\right)\]

\[=\frac{2u\ ^{2}\mbox{sin}\theta\ \mbox{cos}\theta}{g}\]

\[=\frac{u\ ^{2}\mbox{sin}2\theta}{g}\,.\hskip 56.905512pt... \tag{3.23}\]

#### Maximum Height Reached

At the maximum height (\(A\) in figure 3.10) the velocity of the particle is horizontal. The vertical component of velocity is thus, zero at the highest point. The maximum height is the \(y\)-coordinate of the particle when the vertical component of velocity becomes zero.

We have,

\[v_{y}=u_{y}-gt\]

\[=u\ \mbox{sin}\theta-gt.\]

At the maximum height

\[0=u\ \mbox{sin}\theta-gt\]

\[\mbox{or,}\hskip 56.905512ptt=\frac{u\ \mbox{sin}\theta}{g}\,.\hskip 56.905512pt... \tag{3.24}\]

The maximum height is

\[H=u_{y}t-\frac{1}{2}\,gt^{\ 2}\]

\[=(u\ \mbox{sin}\theta)\left(\frac{u\ \mbox{sin}\theta}{g}\right)-\frac{1}{2}\,g\left(\frac{u\ \mbox{sin}\theta}{g}\right)^{\ 2}\]

\[=\frac{u\ ^{2}\mbox{sin}\ ^{2}\theta}{g}-\frac{1}{2}\,\frac{u\ ^{2}\mbox{sin}\ ^{2}\theta}{g}\]

\[=\frac{u\ ^{2}\mbox{sin}\ ^{2}\theta}{2\,g}\,.\hskip 56.905512pt... \tag{3.25}\]

Equation (3.24) gives the time taken in reaching the maximum height. Comparison with equation (3.22) shows that it is exactly half the time of the flight. Thus, the time taken in ascending the maximum height equals the time taken in descending back to the same horizontal plane.

#### Example 3.9

_A ball is thrown from a field with a speed of_ 12\(\cdot\)0 m/s _at an angle of_ 45\({}^{\circ}\) _with the horizontal. At what distance will it hit the field again_? _Take_\(g=10\mbox{$\cdot$}0\) m/s\({}^{\ 2}\).

_Solution :_ The horizontal range \(=\frac{u\ ^{2}\mbox{sin}2\theta}{g}\)

\[=\frac{(12\ \mbox{m/s})^{\ 2}\times\mbox{sin}(2\times 45^{\circ})}{10\ \mbox{m/s}^{\ 2}}\]

\[=\frac{144\ \mbox{m}\ ^{2}/\mbox{s}^{\ 2}}{10\cdot 0\ \mbox{m/s}^{\ 2}}=14\mbox{$\cdot$}4\ \mbox{m}.\]

Thus, the ball hits the field at 14\(\cdot\)4 m from the point of projection.

### Change of Frame

So far we have discussed the motion of a particle with respect to a given frame of reference. The frame can be chosen according to the convenience of the problem. The position \(\stackrel{{\rightarrow}}{{r}}\), the velocity \(\stackrel{{\rightarrow}}{{v}}\) and the acceleration \(\stackrel{{\rightarrow}}{{a}}\) of a particle depend on the frame chosen. Let us see how can we relate the position, velocity and acceleration of a particle measured in two different frames.

Consider two frames of reference \(S\) and \(S^{\prime}\) and suppose a particle \(P\) is observed from both the frames. The frames may be moving with respect to each other. Figure (3.11) shows the situation.

The position vector of the particle \(P\) with respect to the frame \(S\) is \(\overrightarrow{r_{P,\,S}}=\overrightarrow{OP}\). The position vector of the particle with respect to the frame \(S^{\prime}\) is \(\overrightarrow{r_{P,\,S}}=\overrightarrow{OP}\). The position of the frame \(S^{\prime}\) (the origin of frame \(S^{\prime}\) in fact) with respect to the frame \(S\) is \(\mathit{OO}^{\prime}\).

It is clear that

\[\overrightarrow{OP}=\overrightarrow{OO^{\prime}}+\overrightarrow{OP}= \overrightarrow{OP}+\overrightarrow{OO^{\prime}}\] \[\text{or,}\quad\begin{array}{c}\rightarrow\\ \rightarrow\\ \rightarrow\\ \rightarrow\end{array}=\overrightarrow{r_{P,\,S^{\prime}}}\rightarrow\ \

**Solution :**: We have to find the velocity of raindrops with respect to the man. The velocity of the rain as well as the velocity of the man are given with respect to the street. We have

\(\overset{\rightarrow}{v_{\mathit{\min},\mathit{\max}}}=\overset{\rightarrow}{v_{ \mathit{\min},\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit{\mathit}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}\}}\}}}\}}\}}}\}}\}\}}\}\}\}\}\}\}\}\}\}\}\\}\\\}\\\\}\\\\\\}\Thus, the displacement during 0 to 4 s is

\[125\;{\rm m}-5\;{\rm m}=120\;{\rm m}.\]

\[{\rm Average\;velocity}=\frac{120\;{\rm m}}{4\;{\rm s}}=30\;{\rm m/s}.\]

(e) \(v=3{\rm d}t^{\;2}+2Bt+C\).

\[{\rm Velocity\;at}\;t=0\;{\rm is}\;\;C\!=\!-2\;{\rm m/s}.\]

\[{\rm Velocity\;at}\;t=4\;{\rm s}\;{\rm is}\;=78\;{\rm m/s}.\]

\[{\rm Average\;acceleration}=\frac{v_{{}_{2}}-v_{{}_{1}}}{t_{{}_{2}}-t_{{}_{1}}} \!=\!20\;{\rm m/s}^{\;2}.\]

**4.**: _From the velocity-time graph of a particle given in figure (3-WI), describe the motion of the particle qualitatively in the interval \(0\;{\rm to}\;4\;{\rm s}\). Find (a) the distance travelled during first two seconds, (b) during the time \(2\;{\rm s}\;to\;4\;{\rm s}\), (c) during the time \(0\;{\rm to}\;4\;{\rm s}\), (d) displacement during \(0\;{\rm to}\;4\;{\rm s}\), (e) acceleration at \(t=1/2\;{\rm s}\) and (f) acceleration at \(t=2\;{\rm s}\)._

**Solution :**: At \(t=0\), the particle is at rest, say at the origin. After that the velocity is positive, so that the particle moves in the positive \(x\) direction. Its speed increases till 1 second when it starts decreasing. The particle continues to move further in positive \(x\) direction. At \(t\!=\!2\;{\rm s}\), its velocity is reduced to zero, it has moved through a maximum positive \(x\) distance. Then it changes its direction, velocity being negative, but increasing in magnitude. At \(t=3\;{\rm s}\) velocity is maximum in the negative \(x\) direction and then the magnitude starts decreasing. It comes to rest at \(t=4\;{\rm s}\). (a) Distance during \(0\;{\rm to}\;2\;{\rm s}\!=\!{\rm Area\;of}\;OAB\)

\[=\!\frac{1}{2}\times 2\;{\rm s}\times 10\;{\rm m/s}=10\;{\rm m}.\] (b) Distance during \(2\;{\rm to}\;4\;{\rm s}\!=\!{\rm Area\;of}\;BCD=10\;{\rm m}\). The particle has moved in negative \(x\) direction during this period. (c) The distance travelled during \(0\;{\rm to}\;4{\rm s}=10\;{\rm m}+10\;{\rm m}\)\(=20\;{\rm m}\). (d) displacement during \(0\;{\rm to}\;\;4\;{\rm s}=10\;{\rm m}+(-10\;{\rm m})=0\). (e) at \(t=1/2\;{\rm s}\) acceleration = slope of line \(OA=10\;{\rm m/s}^{\;2}\). (f) at \(t=2\;{\rm s}\) acceleration = slope of line \(ABC=-10\;{\rm m/s}^{\;2}\).
**5.**: _A particle starts from rest with a constant acceleration. At a time \(t\) second, the speed is found to be \(100\;{\rm m/s}\) and one second later the speed becomes \(150\;{\rm m/s}\). Find (a) the acceleration and (b) the distance travelled during the (\(t\)+\(1\))\({}^{th}\) second._
**Solution :**: (a) Velocity at time \(t\) second is

\[100\;{\rm m/s}=a.(t\;{\rm second})\;\\[s=\frac{1}{2}\,at^{\ 2}.\]... (i) During this interval the jeep travels a distance \[s+d=vt.\]... (ii) By (i) and (ii), \[\frac{1}{2}\,at^{\ 2}-vt+d=0\] or, \[t=\frac{v\pm\sqrt{v^{\ 2}-2ad}}{a}\.\] The pickpocket will be caught if \(t\) is real and positive. This will be possible if \[v^{\ 2}\geq 2ad\quad\text{or,}\ v\geq\sqrt{2ad}.\]
**8.**: _A car is moving at a constant speed of \(40\) km/h along a straight road which heads towards a large vertical wall and makes a sharp \(90^{\circ}\) turn by the side of the wall. A fly flying at a constant speed of \(100\) km/h, starts from the wall towards the car at an instant when the car is \(20\) km away, flies until it reaches the glasspane of the car and returns to the wall at the same speed. It continues to fly between the car and the wall till the car makes the \(90^{\circ}\) turn. (a) What is the total distance the fly has travelled during this period? (b) How many trips has it made between the car and the wall?_
**Solution :**: (a) The time taken by the car to cover \(20\) km before the turn is \(\frac{20\,\text{km}}{40\text{ km/h}}=\frac{1}{2}\,\text{h}\). The fly moves at a constant speed of \(100\) km/h during this time. Hence the total distance covered by it is \(100\,\frac{\text{km}}{\text{h}}\times\frac{1}{2}\,\text{h}=50\,\text{km}\). (b) Suppose the car is at a distance \(x\) away (at \(A\)) when the fly is at the wall (at \(O\)). The fly hits the glasspane at \(B\), taking a time \(t\). Then \[AB=(40\text{ km/h})t,\] and \[OB=(100\text{ km/h})t.\] Thus, \[x=AB+OB\] \[=(140\text{ km/h})t\] or, \[t=\frac{x}{140\text{ km/h}}\,\text{ or }\ OB=\frac{5}{7}\,x.\]

The fly returns to the wall and during this period the car moves the distance \(BC\). The time taken by the fly in this return path is

\[\left(\frac{5\,x/7}{100\,\text{km/h}}\right)=\frac{x}{140\text{ km/h}}\,.\]

Thus, \[BC=\frac{40\,x}{140}=\frac{2}{7}\,x\]

or, \[OC=OB-BC=\frac{3}{7}\,x.\]

If at the beginning of the round trip (wall to the car and back) the car is at a distance \(x\) away, it is \(\frac{3}{7}\,x\) away when the next trip again starts. Distance of the car at the beginning of the \(1\)st trip \(=20\) km. Distance of the car at the beginning of the \(2\)nd trip

\[=\frac{3}{7}\times 20\text{ km}.\]

Distance of the car at the beginning of the \(3\)rd trip

\[=\left(\frac{3}{7}\right)^{2}\times 20\text{ km}.\]

Distance of the car at the beginning of the \(4\)th trip

\[=\left(\frac{3}{7}\right)^{3}\times 20\text{ km}.\]

Trips will go on till the car reaches the turn that is the distance reduces to zero. This will be the case when \(n\) becomes infinity. Hence the fly makes an infinite number of trips before the car takes the turn.
**9.**: _A ball is dropped from a height of \(19\cdot 6\) m above the ground. It rebounds from the ground and raises itself up to the same height. Take the starting point as the origin and vertically downward as the positive X-axis. Draw approximate plots of \(x\) versus \(t\), \(v\) versus \(t\) and \(a\) versus \(t\). Neglect the small interval during which the ball was in contact with the ground._
**Solution :**: Since the acceleration of the ball during the contact is different from '\(g\)', we have to treat the downward motion and the upward motion separately. For the downward motion : \(a=g=9\cdot 8\) m/s\({}^{2}\), \(x=ut+\frac{1}{2}\,at^{\ 2}=(4\cdot 9\) m/s\({}^{2})t^{\ 2}\). The ball reaches the ground when \(x=19\cdot 6\) m. This gives \(t=2\) s. After that it moves up, \(x\) decreases and at \(t=4\) s, \(x\) becomes zero, the ball reaching the initial point. We have at \(t=0\), \(x=0\) \(t=1\) s, \(x=4\cdot 9\) m \(t=2\) s, \(x=19\cdot 6\) m \(t=3\) s, \(x=4\cdot 9\) m \(t=4\) s, \(x=0\).

Figure 3-W3

**Velocity**: : During the first two seconds,

\(v=u+at=(9\cdot 8\) m/s\({}^{2})t\)

at\(t=0\)

at\(t=1\) s,\(v=9\cdot 8\) m/s

at\(t=2\) s,\(v=19\cdot 6\) m/s.

During the next two seconds the ball goes upward, velocity is negative, magnitude decreasing and at \(t=4\) s, \(v=0\). Thus,

at\(t=2\) s,\(v=-19\cdot 6\) m/s

at\(t=3\) s,\(v=-9\cdot 8\) m/s

at\(t=4\) s,\(v=0\).

At \(t=2\) s there is an abrupt change in velocity from 19\(\cdot 6\) m/s to \(-19\cdot 6\) m/s. In fact this change in velocity takes place over a small interval during which the ball remains in contact with the ground.

**Acceleration :** The acceleration is constant 9\(\cdot 8\) m/s\({}^{2}\) throughout the motion (except at \(t=2\) s).

**10.**: _A stone is dropped from a balloon going up with a uniform velocity of \(5\cdot 0\) m/s. If the balloon was \(50\) m high when the stone was dropped, find its height when the stone hits the ground. Take \(g=10\) m/s\({}^{2}\)._

**Solution**: : At \(t=0\), the stone was going up with a velocity of \(5\cdot 0\) m/s. After that it moved as a freely falling particle with downward acceleration \(g\). Take vertically upward as the positive \(X\)-axis. If it reaches the ground at time \(t\),

\(x=-50\) m, \(u=5\) m/s, \(a=-10\) m/s\({}^{2}\).

We have \(x=ut+\frac{1}{2}at^{2}\)

or, \(-50\) m = (5 m/s). \(t+\frac{1}{2}\times(-10\) m/s\({}^{2})t^{2}\)

or, \(t=\frac{1\pm\sqrt{41}}{2}\) s.

or, \(t=-2\cdot 7\) s or, \(3\cdot 7\) s.

Negative \(t\) has no significance in this problem. The stone reaches the ground at \(t=3\cdot 7\) s. During this time the balloon has moved uniformly up. The distance covered by it is

\(5\) m/s \(\times 3\cdot 7\) s = 18\(\cdot 5\) m.

Hence, the height of the balloon when the stone reaches the ground is \(50\) m + 18\(\cdot 5\) m = 68\(\cdot 5\) m.

**11.**: _A football is kicked with a velocity of \(20\) m/s at an angle of \(45^{\circ}\) with the horizontal. (a) Find the time taken by the ball to strike the ground. (b) Find the maximum height it reaches. (c) How far away from the kick does it hit the ground \(?\) Take \(g=10\) m/s\({}^{2}\)._

**Solution**: : (a) Take the origin at the point where the ball is kicked, vertically upward as the \(Y\)-axis and the horizontal in the plane of motion as the \(X\)-axis. The initial velocity has the components

\(u_{x}=(20\) m/s) cos\(45^{\circ}=10\)\(\backslash 2\) m/s

and \(u_{y}=(20\) m/s) sin\(45^{\circ}=10\)\(\backslash 2\) m/s.

When the ball reaches the ground, \(y=0\).

Using \(y=u_{y}t-\frac{1}{2}gt^{2}\),

\(0=(10\sqrt{2}\) m/s) \(t-\frac{1}{2}\times(10\) m/s\({}^{2})\times t^{2}\)

or, \(t=2\backslash 2\) s = 2\(\cdot 8\) s.

Thus, it takes 2\(\cdot 8\) s for the football to fall on the ground.

(b) At the highest point \(v_{y}=0\). Using the equation

\(v_{y}^{2}=u_{y}^{2}-2\,gy\),

\(0=(10\sqrt{2}\) m/s\()^{2}-2\times(10\) m/s\({}^{2})H\)

or, \(H=10\) m.

Thus, the maximum height reached is \(10\) m.

(c) The horizontal distance travelled before falling to the ground is \(x=u_{x}t\)

\(=(10\sqrt{2}\) m/s) (\(2\sqrt{2}\) s) = 40 m.

**12.**: _A helicopter on flood relief mission, flying horizontally with a speed \(u\) at an altitude H, has to drop a food packet for a victim standing on the ground. At what distance from the victim should the packet be dropped \(?\) The victim stands in the vertical plane of the helicopter's motion._

**Solution :** The velocity of the food packet at the time of release is \(u\) and is horizontal. The vertical velocity at the time of release is zero.

**Vertical motion :** If \(t\) be the time taken by the packet to reach the victim, we have for vertical motion,

\[H = \frac{1}{2}g\,t^{\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,

**14**.: _A projectile is fired with a speed u at an angle th with the horizontal. Find its speed when its direction of motion makes an angle a with the horizontal._
**Solution**: : Let the speed be \(v\) when it makes an angle a with the horizontal. As the horizontal component of velocity remains constant,

\[v\ \cos\alpha = u\ \cos\theta\]

or,

\[v = u\ \cos\theta\ \sec\alpha.\]
**15**.: _A bullet is fired horizontally aiming at an object which starts falling at the instant the bullet is fired. Show that the bullet will hit the object._
**Solution**: : The situation is shown in figure (3-W10). The object starts falling from the point \(B\). Draw a vertical line _BC_ through \(B\). Suppose the bullet reaches the line _BC_ at a point \(D\) and it takes a time \(t\) in doing so.

Consider the vertical motion of the bullet. The initial vertical velocity = 0. The distance travelled vertically = _BD_ = \(\frac{1}{2}\mathit{gt}\)\({}^{2}\). In time \(t\) the object also travels a distance \(\frac{1}{2}\mathit{gt}\)\({}^{2}\) = _BD_. Hence at time \(t\), the object will also be at the same point \(D\). Thus, the bullet hits the object at point \(D\).
**16**.: _A man can swim in still water at a speed of \(3\)_km/h_. He wants to cross a river that flows at \(2\)_km/h_ and reach the point directly opposite to his starting point. (a) In which direction should he try to swim (that is, find the angle his body makes with the river flow)? (b) How much time will he take to cross the river if the river is \(500\)_m _wide_?
**Solution**: : The situation is shown in figure (3-W11). The _X_-axis is chosen along the river flow and the origin at the starting position of the man. The direction of the velocity of man with respect to ground is along the _Y_-axis (perpendicular to the river). We have to find the direction of velocity of the man with respect to water.

Let \(\overset{\rightarrow}{v}_{r,g} = \text{velocity of the river with respect to the ground}\)

\[= 2\ \text{km/h along the }X\text{-axis}\]

\[\overset{\rightarrow}{v}_{m,r} = \text{velocity of the man with respect to the river}\]

\[= 3\ \text{km/h making an angle th with the }Y\text{-axis}\]

and \(\overset{\rightarrow}{v}_{m,g} = \text{velocity of the man with respect to the ground along the }Y\text{-axis}\).

We have \(\overset{\rightarrow}{v}_{m,g} = \overset{\rightarrow}{v}_{m,r} + \overset{\rightarrow}{v}_{r,g}\).... (i) Takingcomponentsalongthe_X_-axis

\[0 = - (3\ \text{km/h})\text{sin}\theta + 2\ \text{km/h}\]

or, \(\text{sin}\theta = \frac{2}{3}\).

(b) Taking components in equation (i) along the _Y_-axis,

\[v_{m,g} = (3\ \text{km/h})\ \text{cos}\theta + 0\]

or, \(v_{m,g} = \sqrt{5}\ \text{km/h}\).

Time = \frac{\text{Displacement in }y\ \text{direction}}{\text{Velocity in }y\ \text{direction}}\]

\[= \frac{0\textless\ \text{km}}{\sqrt{5}\ \text{km/h}} = \frac{\sqrt{5}}{10}\ \text{h}.\]
**17**.: _A man can swim at a speed of \(3\)_km/h _in still water. He wants to cross a \(500\)_m _wide river flowing at \(2\)_km/h_. He keeps himself always at an angle of \(120^{\circ}\) with the river flow while swimming. (a) Find the time he takes to cross the river. (b) At what point on the opposite bank will he arrive_?
**Solution**: : The situation is shown in figure (3-W12).

Here \(\overset{\rightarrow}{v}_{r,g}\) = velocity of the river with respect to the ground \(\overset{\rightarrow}{v}_{m,r}\) = velocity of the man with respect to the river \(\overset{\rightarrow}{v}_{m,g}\) = velocity of the man with respect to the ground.

Figure 3-W12

Figure 3-W11

Figure 3-W10(a) We have,

\[\overset{\rightarrow}{v}_{m,g}=\overset{\rightarrow}{v}_{m,r}+\overset{\rightarrow}{v}_{r,g}\qquad\qquad\qquad\ldots\] (i)

Hence, the velocity with respect to the ground is along _AC_. Taking \(y\)-components in equation (i),

\[\overset{\rightarrow}{v}_{m,g}\sin\theta=3\text{ km/h cos}30^{\circ}+2\text{ km/h cos}90^{\circ}=\frac{3\sqrt{3}}{2}\text{ km/h}.\]

Time taken to cross the river

\[=\frac{\text{displacement along the $Y$-axis}}{\text{velocity along the $Y$-axis}}\]

\[=\frac{1/2\text{ km}}{3\sqrt{3/2}\text{ km/h}}=\frac{1}{3/3}\text{ h}.\] (b) Taking \(x\)-components in equation (i),

\[\overset{\rightarrow}{v}_{m,g}\cos\theta=-3\text{ km/h sin}30^{\circ}+2\text{ km/h}\]

\[=\frac{1}{2}\text{ km/h}.\]

Displacement along the \(X\)-axis as the man crosses the river

\[=(\text{velocity along the $X$-axis})\cdot(\text{time})\]

\[=\left(\frac{1}{2\text{ h}}\right)\times\left(\frac{1}{3\sqrt{3}}\text{ h}\right)=\frac{1}{6\sqrt{3}}\text{ km}.\]
**18**: _A man standing on a road has to hold his umbrella at \(30^{\circ}\) with the vertical to keep the rain away. He throws the umbrella and starts running at \(10\text{ km/h}\). He finds that raindrops are hitting his head vertically. Find the speed of raindrops with respect to (a) the road, (b) the moving man._
**Solution :**: When the man is at rest with respect to the ground, the rain comes to him at an angle \(30^{\circ}\) with the vertical. This is the direction of the velocity of raindrops with respect to the ground. The situation when the man runs is shown in the figure (3-W13b).

Taking vertical components, equation (i) gives

\[v_{r,g}\cos 30^{\circ}=v_{r,m}\]

or, \[v_{r,m}=(20\text{ km/h})\cdot\frac{\sqrt{3}}{2}\]

\[=10\sqrt{3}\text{ km/h}.\]
**19**: _A man running on a horizontal road at \(8\text{ km/h}\) finds the rain falling vertically. He increases his speed to \(12\text{ km/h}\) and finds that the drops make angle \(30^{\circ}\) with the vertical. Find the speed and direction of the rain with respect to the road._
**Solution :**:

We have

\[\overset{\rightarrow}{v}_{min,\,road}=\overset{\rightarrow}{v}_{min,\,max}+ \overset{\rightarrow}{v}_{max,\,road}\qquad\qquad\ldots\] (i)

The two situations given in the problem may be represented by the following figure.

\(v_{rain,\,road}\) is same in magnitude and direction in both the figures.

Taking horizontal components in equation (i) for figure (3-W14a),

\[v_{rain,\,road}\text{ sin}\alpha=8\text{ km/h}.\qquad\qquad\ldots\] (ii)

Now consider figure (3-W14b). Draw a line \(OA\perp v_{rain,\,man}\) as shown.

Taking components in equation (i) along the line \(OA\).

\(v_{rain,\,road}\sin(30^{\circ}+\alpha)=12\text{ km/h cos}30^{\circ}.\qquad\qquad\ldots\) (iii)

From (ii) and (iii),

\[\frac{\sin(30^{\circ}+\alpha)}{\text{sin}\alpha}=\frac{12\times\sqrt{3}}{8 \times 2}\]

or, \[\frac{\sin 30^{\circ}\text{cos}\alpha+\cos 30^{\circ}\text{sin}\alpha}{\text{sin}\alpha}=\frac{3\sqrt{3}}{4}\]

or, \[\frac{1}{2}\text{cot}\alpha+\frac{\sqrt{3}}{2}=\frac{3\sqrt{3}}{4}\]

or, \[\cot\alpha=\frac{\sqrt{3}}{2}\]

or, \[\alpha=\cot^{-1}\frac{\sqrt{3}}{2}\,.\]

From (ii),

\[v_{rain,\,road}=\frac{8\text{ km/h}}{\text{sin}\alpha}=4\sqrt{7}\text{ km/h}.\]
**20**: _Three particles \(A\), \(B\) and \(C\) are situated at the vertices of an equilateral triangle ABC of side \(d\) at \(t=0\). Each

Figure 3-W14

of the particles moves with constant speed v. A always has its velocity along AB, B along BC and C along CA. At what time will the particles meet each other_?
**Solution :**: The motion of the particles is roughly sketched in figure (3-W15).

By symmetry they will meet at the centroid \(O\) of the triangle. At any instant the particles will form an equilateral triangle \(ABC\) with the same centroid \(O\). Concentrate on the motion of any one particle, say \(A\). At any instant its velocity makes angle \(30^{\circ}\) with \(AO\).

The component of this velocity along \(AO\) is \(v\) cos30\({}^{\circ}\). This component is the rate of decrease of the distance \(AO\). Initially,

\[AO=\frac{2}{3}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \12. A player hits a baseball at some angle. The ball goes high up in space. The player runs and catches the ball before it hits the ground. Which of the two (the player or the ball) has greater displacement?
13. The increase in the speed of a car is proportional to the additional petrol put into the engine. Is it possible to accelerate a car without putting more petrol or less petrol into the engine?
14. Rain is falling vertically. A man running on the road keeps his umbrella tilted but a man standing on the street keeps his umbrella vertical to protect himself from the rain. But both of them keep their umbrella vertical to avoid the vertical sun-rays. Explain.

## Objective

1. A motor car is going due north at a speed of 50 km/h. It makes a 90\({}^{\circ}\) left turn without changing the speed. The change in the velocity of the car is about 1. 50 km/h towards west 2. 70 km/h towards south-west 3. 70 km/h towards north-west 4. zero.
2. Figure (3-Q2) shows the displacement-time graph of a particle moving on the _X_-axis. (a) the particle is continuously going in positive \(x\) direction (b) the particle is at rest (c) the velocity increases up to a time _t_o, and then becomes constant (d) the particle moves at a constant velocity up to a time _t_o, and then stops.
3. A particle has a velocity \(u\) towards east at \(t\) = 0. Its acceleration is towards west and is constant. Let \(x_{\text{a}}\) and \(x_{\text{B}}\) be the magnitude of displacements in the first 10 seconds and the next 10 seconds (a) \(x_{\text{a}}<x_{\text{B}}\) (b) \(x_{\text{a}}=x_{\text{B}}\) (c) \(x_{\text{A}}>x_{\text{B}}\) (d) the information is insufficient to decide the relation of \(x_{\text{A}}\) with \(x_{\text{B}}\).
4. A person travelling on a straight line moves with a uniform velocity \(v_{\text{i}}\) for some time and with uniform velocity \(v_{\text{z}}\) for the next equal time. The average velocity \(v\) is given by 1. \(v=\frac{v_{\text{i}}+v_{\text{z}}}{2}\) 2. \(v=\sqrt[]{v_{\text{i}}v_{\text{z}}}\) 3. \(v=\frac{1}{v_{\text{i}}}+\frac{1}{v_{\text{z}}}\) 4. A person travelling on a straight line moves with a uniform velocity \(v_{\text{i}}\) for a distance \(x\) and with a uniform velocity \(v_{\text{z}}\) for the next equal distance. The average velocity \(v\) is given by 1. \(v=\frac{v_{\text{i}}+v_{\text{z}}}{2}\) 2. \(v=\sqrt[]{v_{\text{i}}v_{\text{z}}}\) 4. A person travelling on a straight line moves with a uniform velocity \(v_{\text{i}}\) for a distance \(x\) and with a uniform velocity \(v_{\text{z}}\) for the next equal distance. The average velocity \(v\) is given by 1. \(v=\frac{v_{\text{i}}+v_{\text{z}}}{2}\) 2. \(v=\frac{1}{v_{\text{i}}}+\frac{1}{v_{\text{z}}}\) 3. \(v=\frac{1}{v_{\text{i}}}+\frac{1}{v_{\text{z}}}\) 4. A store is released from an elevator going up with an acceleration \(a\). The acceleration of the stone after the release is 1. \(a\) upward 2. \(v=\sqrt[]{v_{\text{i}}v_{\text{z}}}\) 3. \(v=\frac{1}{v_{\text{i}}}+\frac{1}{v_{\text{z}}}\) 4. A person standing near the edge of the top of a building throws two balls \(A\) and \(B\). The ball \(A\) is thrown vertically upward and \(B\) is thrown vertically downward with the same speed. The ball \(A\) hits the ground with a speed \(v_{\text{A}}\) and the ball \(B\) hits the ground with a speed \(v_{\text{B}}\). We have 1. \(v_{\text{A}}>v_{\text{B}}\), 2. \(v_{\text{A}}<v_{\text{B}}\) (c) \(v_{\text{A}}=v_{\text{B}}\) 4. the relation between \(v_{\text{A}}\) and \(v_{\text{B}}\) depends on height of the building above the ground.
5. In a projectile motion the velocity 1. is always perpendicular to the acceleration 2. is never perpendicular to the acceleration 3. is perpendicular to the acceleration for one instant only 4. is perpendicular to the acceleration for two instants.
6. Two bullets are fired simultaneously, horizontally and with different speeds from the same place. Which bullet will hit the ground first? 1. the faster one 2. the slower one 3. both will reach simultaneously 4. depends on the masses.
7. The range of a projectile fired at an angle of 15\({}^{\circ}\) is 50 m. If it is fired with the same speed at an angle of 45\({}^{\circ}\), its range will be 1. 2. \(v=\frac{1}{v_{\text{i}}}+\frac{1}{v_{\text{z}}}\) 4. A person travelling on a straight line moves with a uniform velocity \(v_{\text{i}}\) for a distance \(x\) and with a uniform velocity \(v_{\text{z}}\) for the next equal distance. The average velocity \(v\) is given by 1. \(v=\frac{1}{v_{\text{i}}}+\frac{1}{v_{\text{z}}}\) 5. A person travelling on a straight line moves with a uniform velocity \(v_{\text{z}}\) for a distance \(x\) and with a uniform velocity \(v_{\text{z}}\) for the next equal distance. The average velocity \(v\) is given by 1. \(v=\frac{1}{v_{\text{z}}}+\frac{1}{v_{\text{z}}}\) 6. A person travelling on a straight line moves with a uniform velocity \(v_{\text{z}}\) for a distance \(x\) and with a uniform velocity \(v_{\text{z}}\) for the next equal distance. The average velocity \(v\) is given by 1. \(v=\frac{1}{v_{\text{z}}}+\frac{1}{v_{\text{z}}}\) 7. A person travelling on a straight line moves with a uniform velocity \(v_{\text{z}}\) for a distance \(x\) and with a uniform velocity \(v_{\text{z}}\) for the next equal distance. The average velocity \(v\) is given by 1. \(v=\frac{1}{v_{\text{z}}}+\frac{1}{v_{\text{z}}}\) 8. A person travelling on a straight line moves with a uniform velocity \(v_{\text{z}}\) for a distance \(x\) and with a uniform velocity \(v_{\text{z}}\) for the next equal distance. The average velocity \(v\) is given by 1. \(v=\frac{1}{v_{\text{z}}}+\frac{1}{v_{\text{z}}}\) 9. A person travelling on a straight line moves with a uniform velocity \(v_{\text{z}}\) for a distance \(x\) and with a uniform velocity \(v_{\text{z}}\) for the next equal distance. The average velocity \(v\) is given by 1. \(v=\frac{1}{v_{\text{z}}}+\frac{1}{v_{\text{z}}}\) 10. A person travelling on a straight line moves with a uniform velocity \(v_{\text{z}}\) for a distance \(x\) and with a uniform velocity \(v_{\text{z}}\) for the next equal distance. The average velocity \(v\) is given by 1. \(v=\frac{1}{v_{\text{z}}}+\frac{1}{v_{\text{z}}}\) 11. A person travelling on a straight line moves with a uniform velocity \(v_{\text{z}}\) for a distance \(x\) and with a uniform velocity \(v_{\text{z}}\) for the next equal distance. The average velocity \(v\) is given by 1. \(v=\frac{1}{v_{\text{z}}}+\frac{1}{v_{\text{z}}}\) 12. A person travelling on a straight line moves with a uniform velocity \(v_{\text{z}}\) for a distance \(x\) and with a uniform velocity \(v_{\text{z}}\) for the next equal distance. The average velocity \(v\) is given by 1.

[MISSING_PAGE_POST]

he acceleration at \(t=0\) must be zero. 2. [label=()]
52. [label=()]
53. The acceleration of the particle is \(a\) 2. [label=()]
54. [label=()]
55. [label=()]
56. [label=()]
57. [label=()]
58. [label=()]
59. The acceleration of the particle is \(a\) 2. [label=()]
60. [label=()]
61. [label=()]
62. [label=()]
63. The average velocity in an interval is equal to its average speed in that interval. 1. [label=()]
64. [label=()]
65. It is possible to have a situation in which the speed of a particle is always zero but the average speed is not zero. 1. [label=()]
66. It is possible to have a situation in which the speed of the particle is never zero but the average speed in an interval is zero.
70. [label=()]
71. [label=()]
72. The velocity-time plot for a particle moving on a straight line is shown in the figure (3-3).
73. [label=()]
74. [label=()]
75. [label=()]
76. The particle has a constant acceleration. 1. [label=()]
77. [label=()]
78. [label=()]
79. The particle has never turned around. 1. [label=()]
79. The particle has zero displacement. 1. [label=()]
71. [label=()]
72. The average speed in the interval \(0\) to \(t=6\,\mathrm{s}\). 10. [label=()]
73. The average velocity for the total period shown is negative.

Figure 3-3

Figure 4

Figure 5-

Figure 6

Figure 7-

[MISSING_PAGE_POST]

**1.**: A man has to go 50 m due north, 40 m due east and 20 m due south to reach a field. (a) What distance he has to walk to reach the field? (b) What is his displacement from his house to the field?
**2.**: A particle starts from the origin, goes along the _X_-axis to the point (20 m, 0) and then returns along the same line to the point (-20 m, 0). Find the distance and displacement of the particle during the trip.
**3.**: It is 260 km from Patna to Ranchi by air and 320 km by road. An aeroplane takes 30 minutes to go from Patna to Ranchi whereas a delux bus takes 8 hours. (a) Find the average speed of the plane. (b) Find the average speed of the bus. (c) Find the average velocity of the plane. (d) Find the average velocity of the bus.
**4.**: When a person leaves his home for sightseeing by his car, the meter reads 12352 km. When he returns home after two hours the reading is 12416 km. (a) What is the average speed of the car during this period? (b) What is the average velocity?
**5.**: An athelete takes 2\(\cdot\)0 s to reach his maximum speed of 18\(\cdot\)0 km/h. What is the magnitude of his average acceleration?
**6.**: The speed of a car as a function of time is shown in figure (3-E1). Find the distance travelled by the car in 8 seconds and its acceleration.
**7.**: The acceleration of a cart started at \(t=0\), varies with time as shown in figure (3-E2). Find the distance travelled in 30 seconds and draw the position-time graph.
**8.**: Figure (3-E3) shows the graph of velocity versus time for a particle going along the _X_-axis. Find (a) the distance traveled by the particle during the first 40 seconds.
**10.**: From the velocity-time plot shown in figure (3-E5), find the distance travelled by the particle during the first 40 seconds.
**11.**: The acceleration of a particle as seen from two frames \(S_{1}\) and \(S_{2}\) have equal magnitude 4 m/s\({}^{2}\).
**12.**: The frames must be at rest with respect to each other.
**13.**: The frames may be moving with respect to each other but neither should be accelerated with respect to the other.
**14.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may either be zero or 8 m/s\({}^{2}\).
**15.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).

**16.**: The acceleration of a particle as seen from two frames \(S_{1}\) and \(S_{2}\) have equal magnitude 4 m/s\({}^{2}\).
**17.**: The frames must be at rest with respect to each other.
**18.**: The frames may be moving with respect to each other but neither should be accelerated with respect to the other.
**19.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may either be zero or 8 m/s\({}^{2}\).
**20.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**21.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**22.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**23.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**24.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**25.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**26.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**27.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**28.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**29.**: Figure (3-E4) shows the graph of the _x_-coordinate of a particle going along the _X_-axis as a function of time. Find (a) the average velocity during 0 to 10 s, (b) instantaneous velocity at 2, 5, 8 and 12s.

**20.**: From the velocity-time plot shown in figure (3-E5), find the distance travelled by the particle during the first 40 seconds.
**21.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**22.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**23.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**24.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**25.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**26.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**27.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**28.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**29.**: Figure (3-E4) shows the graph of the _x_-coordinate of a particle going along the _X_-axis as a function of time. Find (a) the average velocity during 0 to 10 s, (b) instantaneous velocity at 2, 5, 8 and 12s.

**20.**: From the velocity-time plot shown in figure (3-E5), find the distance travelled by the particle during the first 40 seconds.
**21.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**22.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**23.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**24.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**25.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**26.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**27.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**28.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**29.**: Figure (3-E4) shows the graph of the _x_-coordinate of a particle going along the _X_-axis as a function of time. Find (a) the average velocity during 0 to 10 s, (b) instantaneous velocity at 2, 5, 8 and 12s.

**20.**: From the velocity-time plot shown in figure (3-E5), find the distance travelled by the particle during the first 40 seconds.
**22.**: From the velocity-time plot shown in figure (3-E5), find the distance traveled by the particle during the first 40 seconds.
**23.**: From the velocity-time plot shown in figure (3-E5), find the distance traveled by the particle during the first 40 seconds.

**24.**: From the velocity-time plot shown in figure (3-E5), find the distance traveled by the particle during the first 40 seconds.

**25.**: From the velocity-time plot shown in figure (3-E5), find the distance traveled by the particle during the first 40 seconds.

**26.**: From the velocity-time plot shown in figure (3-E5), find the distance traveled by the particle during the first 40 seconds.

**27.**: The acceleration of \(S_{2}\) with respect to \(S_{1}\) may be anything between zero and 8 m/s\({}^{2}\).
**28.**: From the velocity-time plot shown in figure (3-E5), find the distance traveled by the particle during the first 40 seconds.

**29.**: Figure (3-E5) shows the graph of the _x_-coordinate of a particle going along the _X_-axis as a function of time. Find (a) the average velocity during 0 to 10 s, (b) instantaneous velocity at 2, 5, 8 and 12s.

[MISSING_PAGE_POST]

**49.**: Figure (3-E5) shows the graph of the _x_-coordinate of a particle going along the _X_-axis as a function of time. Find (a) the average velocity during 0 to 10 s, (b) instantaneous velocity at 2, 5, 8 and 12s.

**50.**: From the velocity-time plot shown in figure (3-E5), find the distance traveled by the particle during the first 40 seconds.

**51.**: From the velocity-time plot shown in figure (3-E5), find the distance traveled by the particle during the first 40 seconds.

**52.**: From the velocity-time plot shown in figure (3-E5), find the distance traveled by the particle during the first 40 seconds.

**53.**: From the velocity-time plot shown in figure (3-E5), find the distance traveled by the particle during the first 40 seconds.

**54.**: From the velocity-time plot shown in figure (3-E5), find the distance traveled by the particle during the first 40 seconds.

**55seconds. Also find the average velocity during this period.

11. Figure (3-E6) shows \(x\)-\(t\) graph of a particle. Find the time \(t\) such that the average velocity of the particle during the period 0 to \(t\) is zero.
12. A particle starts from a point \(A\) and travels along the solid curve shown in figure (3-E7). Find approximately the position \(B\) of the particle such that the average velocity between the positions \(A\) and \(B\) has the same direction as the instantaneous velocity at \(B\).
13. An object having a velocity 4\(\cdot\)0 m/s is accelerated at the rate of 1\(\cdot\)2 m/s\({}^{2}\) for 5\(\cdot\)0 s. Find the distance travelled during the period of acceleration.
14. A person travelling at 43\(\cdot\)2 km/h applies the brake giving a deceleration of 6\(\cdot\)0 m/s\({}^{2}\) to his scooter. How far will it travel before stopping?
15. A train starts from rest and moves with a constant acceleration of 2\(\cdot\)0 m/s\({}^{2}\) for half a minute. The brakes are then applied and the train comes to rest in one minute. Find (a) the total distance moved by the train, (b) the maximum speed attained by the train and (c) the position(s) of the train at half the maximum speed.
16. A bullet travelling with a velocity of 16 m/s penetrates a tree trunk and comes to rest in 0\(\cdot\)4 m. Find the time taken during the retardation.
17. A bullet going with speed 350 m/s enters a concrete wall and penetrates a distance of 5\(\cdot\)0 cm before coming to rest. Find the deceleration.
18. A particle starting from rest moves with constant acceleration. If it takes 5\(\cdot\)0 s to reach the speed 18\(\cdot\)0 km/h find (a) the average velocity during this period, and (b) the distance travelled by the particle during this period.
19. A driver takes 0\(\cdot\)20 s to apply the brakes after he sees a need for it. This is called the reaction time of the driver. If he is driving a car at a speed of 54 km/h and the brakes cause a deceleration of 6\(\cdot\)0 m/s\({}^{2}\), find the distance travelled by the car after he sees the need to put the brakes on.
20. Complete the following table :

\begin{tabular}{|l|l|l|} \hline  & \multicolumn{1}{c|}{Driver \(X\)} & \multicolumn{1}{c|}{Driver \(Y\)} \\ Car Model & Reaction time 0\(\cdot\)20 s & Reaction time 0\(\cdot\)30 s \\ \hline \(A\) (deceleration & Speed = 54 km/h & Speed = 72 km/h \\ on hard braking & Braking distance & Braking distance \\ = 6\(\cdot\)0 m/s\({}^{2}\)) & \(a\) =................ & \(e\) =................ \\  & Total stopping distance & Total stopping distance \\  & \(f\) =................ & \(h\) =................ \\ \hline \end{tabular}
21. A police jeep is chasing a culprit going on a motorbike. The motorbike crosses a turning at a speed of 72 km/h. The jeep follows it at a speed of 90 km/h, crossing the turning ten seconds later than the bike. Assuming that they travel at constant speeds, how far from the turning will the jeep catch up with the bike?
22. A car travelling at 60 km/h overtakes another car travelling at 42 km/h. Assuming each car to be 5\(\cdot\)0 m long, find the time taken during the overtake and the total road distance used for the overtake.
23. A ball is projected vertically upward with a speed of 50 m/s. Find (a) the maximum height, (b) the time to reach the maximum height, (c) the speed at half the maximum height. Take \(g\) = 10 m/s\({}^{2}\).
24. A ball is dropped from a balloon going up at a speed of 7 m/s. If the balloon was at a height 60 m at the time of dropping the ball, how long will the ball take in reaching the ground?
25. A stone is thrown vertically upward with a speed of 28 m/s. (a) Find the maximum height reached by the stone. (b) Find its velocity one second before it reaches the maximum height. (c) Does the answer of part (b) change if the initial speed is more than 28 m/s such as 40 m/s or 80 m/s?
26. A person sitting on the top of a tall building is dropping balls at regular intervals of one second. Find the positions of the 3rd, 4th and 5th ball when the 6th ball is being dropped.

Figure 3-E6

Figure 4-E7

27. A healthy youngman standing at a distance of 7 m from a 11\(\cdot\)8 m high building sees a kid slipping from the top floor. With what speed (assumed uniform) should he run to catch the kid at the arms height (1\(\cdot\)8 m)?
28. An NCC parade is going at a uniform speed of 6 km/h through a place under a berry tree on which a bird is sitting at a height of 12\(\cdot\)1 m. At a particular instant the bird drops a berry. Which cadet (give the distance from the tree at the instant) will receive the berry on his uniform?
29. A ball is dropped from a height. If it takes 0\(\cdot\)200 s to cross the last 6\(\cdot\)00 m before hitting the ground, find the height from which it was dropped. Take \(g=10\) m/s\({}^{2}\).
30. A ball is dropped from a height of 5 m onto a sandy floor and penetrates the sand up to 10 cm before coming to rest. Find the retardation of the ball in sand assuming it to be uniform.
31. An elevator is descending with uniform acceleration. To measure the acceleration, a person in the elevator drops a coin at the moment the elevator starts. The coin is 6 ft above the floor of the elevator at the time it is dropped. The person observes that the coin strikes the floor in 1 second. Calculate from these data the acceleration of the elevator.
32. A ball is thrown horizontally from a point 100 m above the ground with a speed of 20 m/s. Find (a) the time it takes to reach the ground, (b) the horizontal distance it travels before reaching the ground, (c) the velocity (direction and magnitude) with which it strikes the ground.
33. A ball is thrown at a speed of 40 m/s at an angle of 60\({}^{\circ}\) with the horizontal. Find (a) the maximum height reached and (b) the range of the ball. Take \(g=10\) m/s\({}^{2}\).
34. In a soccer practice session the football is kept at the centre of the field 40 yards from the 10 ft high goalposts. A goal is attempted by kicking the football at a speed of 64 ft/s at an angle of 45\({}^{\circ}\) to the horizontal. Will the ball reach the goal post?
35. A popular game in Indian villages is _goli_ which is played with small glass balls called golis. The goli of one player is situated at a distance of 2\(\cdot\)0 m from the goli of the second player. This second player has to project his goli by keeping the thumb of the left hand at the place of his goli, holding the goli between his two middle fingers and making the throw. If the projected goli hits the goli of the first player, the second player wins. If the height from which the goli is projected is 19\(\cdot\)6 cm from the ground and the goli is to be projected horizontally, with what speed should it be projected so that it directly hits the stationary goli without falling on the ground earlier?
36. Figure (3-5) shows a 11\(\cdot\)7 ft wide ditch with the approach roads at an angle of 15\({}^{\circ}\) with the horizontal. With what minimum speed should a motorbike be moving on the road so that it safely crosses the ditch? Assume that the length of the bike is 5 ft, and it leaves the road when the front part runs out of the approach road.
37. A person standing on the top of a cliff 171 ft high has to throw a packet to his friend standing on the ground 228 ft horizontally away. If he throws the packet directly aiming at the friend with a speed of 15\(\cdot\)0 ft/s, how short will the packet fall?
38. A ball is projected from a point on the floor with a speed of 15 m/s at an angle of 60\({}^{\circ}\) with the horizontal. Will it hit a vertical wall 5 m away from the point of projection and perpendicular to the plane of projection without hitting the floor? Will the answer differ if the wall is 22 m away?
39. Find the average velocity of a projectile between the instants it crosses half the maximum height. It is projected with a speed \(u\) at an angle 0 with the horizontal.
40. A bomb is dropped from a plane flying horizontally with uniform speed. Show that the bomb will explode vertically below the plane. Is the statement true if the plane flies with uniform speed but not horizontally?
41. A boy standing on a long railroad car throws a ball straight upwards. The car is moving on the horizontal road with an acceleration of 1 m/s\({}^{2}\) and the projection velocity in the vertical direction is 9\(\cdot\)8 m/s. How far behind the boy will the ball fall on the car?
42. A staircase contains three steps each 10 cm high and 20 cm wide (figure 3-5). What should be the minimum horizontal velocity of a ball rolling off the uppermost plane so as to hit directly the lowest plane?
43. A person is standing on a truck moving with a constant velocity of 14\(\cdot\)7 m/s on a horizontal road. The man throws a ball in such a way that it returns to the truck after the truck has moved 58\(\cdot\)8 m. Find the speed and the angle of projection (a) as seen from the truck, (b) as seen from the road.
44. The benches of a gallery in a cricket stadium are 1 m wide and 1 m high. A batsman strikes the ball at a level one metre above the ground and hits a mammoth sixer. The ball starts at 35 m/s at an angle of 53\({}^{\circ}\) with the horizontal. The benches are perpendicular to the plane of motion and the first bench is 110 m from the batsman. On which bench will the ball hit?
45. A man is sitting on the shore of a river. He is in the line of a 1\(\cdot\)0 m long boat and is 5\(\cdot\)5 m away from the centre of the boat. He wishes to throw an apple into the boat. If he can throw the apple only with a speed of 10 m/s, find the minimum and maximum angles of projection for successful shot. Assume that the point of

[MISSING_PAGE_POST]

projection and the edge of the boat are in the same horizontal level.
46. A river 400 m wide is flowing at a rate of 2\(\cdot\)0 m/s. A boat is sailing at a velocity of 10 m/s with respect to the water, in a direction perpendicular to the river. (a) Find the time taken by the boat to reach the opposite bank. (b) How far from the point directly opposite to the starting point does the boat reach the opposite bank?
47. A swimmer wishes to cross a 500 m wide river flowing at 5 km/h. His speed with respect to water is 3 km/h. (a) If he heads in a direction making an angle th with the flow, find the time he takes to cross the river. (b) Find the shortest possible time to cross the river.
48. Consider the situation of the previous problem. The man has to reach the other shore at the point directly opposite to his starting point. If he reaches the other shore somewhere else, he has to walk down to this point. Find the minimum distance that he has to walk.
49. An aeroplane has to go from a point \(A\) to another point \(B\), 500 km away due 30\({}^{\circ}\) east of north. A wind is blowing due north at a speed of 20 m/s. The air-speed of the plane is 150 m/s. (a) Find the direction in which the pilot should head the plane to reach the point \(B\). (b) Find the time taken by the plane to go from \(A\) to \(B\).
50. Two friends \(A\) and \(B\) are standing a distance \(x\) apart in an open field and wind is blowing from \(A\) to \(B\). \(A\) beats a drum and \(B\) hears the sound \(t_{1}\) time after he sees the event. \(A\) and \(B\) interchange their positions and the experiment is repeated. This time \(B\) hears the drum \(t_{2}\) time after he sees the event. Calculate the velocity of sound in still air \(v\) and the velocity of wind \(u\). Neglect the time light takes in travelling between the friends.
51. Suppose \(A\) and \(B\) in the previous problem change their positions in such a way that the line joining them becomes perpendicular to the direction of wind while maintaining the separation \(x\). What will be the time lag \(B\) finds between seeing and hearing the drum beating by \(A\)?
52. Six particles situated at the corners of a regular hexagon of side \(a\) move at a constant speed \(v\). Each particle maintains a direction towards the particle at the next corner. Calculate the time the particles will take to meet each other.

\(\sqcap\)\(\sqcup\)

## Answers

1. (a) 110 m (b) 50 m, \(\tan^{-1}\) 3/4 north to east
2. 60 m, 20 m in the negative direction
3. (a) 520 km/h (b) 40 km/h (c) 520 km/h Patna to Ranchi
4. 32\({}^{\circ}\) km/h Patna to Ranchi
5. 2\({}^{\circ}\) m/s\({}^{2}\)
6. 80 m, 2\({}^{\circ}\) m/s\({}^{2}\)
7. 1000 ft
8. (a) 0\(\cdot\)6 m/s\({}^{2}\) (b) 50 m (c) 50 m
9. (a) 10 m/s (b) 20 m/s, zero, 20 m/s, - 20 m/s
10. 100 m, zero
11. 12 s
12. \(x\) = 5 m, \(y\) = 3 m
13. 35 m
14. 12 m
15. (a) 2\(\cdot\)7 km (b) 60 m/s (c) 225 m and 2\(\cdot\)25 km
16. 0\({}^{\circ}\)5 s
17. 12\({}^{\circ}\)2 \(\times\) 10\({}^{\circ}\) m/s\({}^{2}\)
18. (a) 2\(\cdot\)5 m/s (b) 12\({}^{\circ}\)5 m
19. 22 m
20. (a) 19 m (b) 22 m (c) 33 m (d) 39 m (e) 15 m (f) 18 m (g) 27 m (h) 33 m
21. 1\({}^{\circ}\)0 km
22. 2 s, 38 m
23. (a) 125 m (b) 5 s (c) 35 m/s
24. 4\({}^{\circ}\)3 s
25. (a) 40 m (b) 9\(\cdot\)8 m/s (c) No
26. 44\({}^{\circ}\)1 m, 19\({}^{\circ}\)6 m and 4\(\cdot\)9 m below the top
27. 4\(\cdot\)9 m/s
28. 2\({}^{\circ}\)62 m
29. 48 m
30. 490 m/s\({}^{2}\)
31. 20 f/s\({}^{2}\)
32. (a) 4\(\cdot\)5 s (b) 90 m (c) 49 m/s, th = 66\({}^{\circ}\) with horizontal
33. (a) 60 m (b) 80\(\backslash\)3 m
34. Yes
35. 10 m/s
36. 32 f/s37. 192 ft
38. Yes, Yes
39. \(u\) cos\(\theta\), horizontal in the plane of projection
41. 2 m
42. 2 m/s
43. (a) 19*6 m/s upward (b) 24*5 m/s at 53\({}^{\circ}\) with horizontal
44. Sixth
45. Minimum angle 15\({}^{\circ}\), maximum angle 75\({}^{\circ}\) but there is an interval of 53\({}^{\circ}\) between 15\({}^{\circ}\) and 75\({}^{\circ}\), which is not allowed for successful shot
46. (a) 40 s
47. (a) \(\frac{10\text{ minutes}}{\sin\theta}\) (b) 10 minutes
48. 2/3 km
49. (a) \(\sin^{-1}\) (1/15) east of the line \(AB\) (b) 50 min
50. \(\frac{x}{2}\bigg{(}\frac{1}{t_{1}}+\frac{1}{t_{2}}\bigg{)}\)\(\frac{x}{2}\bigg{(}\frac{1}{t_{1}}-\frac{1}{t_{2}}\bigg{)}\)
51. \(\frac{x}{\sqrt{{{v_{{}^{2}}}}-{u^{{}^{2}}}}}\)
52. \(2\,a/v\).
