{\rtf1\ansi\ansicpg1252\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from mpl_toolkits.mplot3d import axes3d\
import matplotlib.pyplot as plt\
\
\
chart = plt.figure()\
chart3d = chart.add_subplot(111, projection='3d')\
\
# Create some test data.\
X, Y, Z = axes3d.get_test_data(0.08)\
\
# Plot a wireframe.\
chart3d.plot_wireframe(X, Y, Z, color='r',rstride=15, cstride=10)\
\
plt.show()}