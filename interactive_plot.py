{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "X = pd.read_csv(\"./Linear_X_Train.csv\").values\n",
    "Y = pd.read_csv(\"./Linear_Y_Train.csv\").values\n",
    "\n",
    "theta = np.load(\"Theta_List.npy\")\n",
    "\n",
    "T0 = theta[:,0]\n",
    "T1 = theta[:,1]\n",
    "\n",
    "plt.ion()\n",
    "for i in range(0,50,3):\n",
    "    y_ = T1[i]*X + T0\n",
    "    plt.scatter(X,Y) #pints\n",
    "    plt.plot(X,y_,'red')  #line\n",
    "    plt.draw()\n",
    "    plt.pause(1) # pause the graph\n",
    "    plt.clf()  # destroys previous plots"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
