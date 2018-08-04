# ZeroWaste

![](https://github.com/naivelogic/ZeroWaste/blob/master/image_prep/support/ZeroWasteLogo1%20(2).png)
_Saving the world, one item at a time_

__Zero Waste Vision:__ Zero Waste is a tool to enable the Microsoft community to reduce waste. Using an IoT device backed by an AI system, Zero Waste identifies and classifies objects as compostable, recyclable or landfill in real time as people throw objects into a waste bin. The real value of Zero Waste is to provide real time indicators via LEDs located on the waste bins to enable reinforce learning to those throwing the objects away to reduce waste. The reinforcement in waste behavior work as follows: when an object such as an aluminum can is thrown in the landfill bin, a red LED will be indicated on the landfill bin and a green LED on the recycling bin. In this way we can have a positive feedback mechanism for correcting the waste disposal behavior within the Microsoft community. This will not only have positive environmental effects but also beneficial economic effects.

__What it does (Current State):__ Zero Waste provide real time image recognition to assist sorting waste into their corresponding categories. The LED reinforcement learning is still under development. 

__Problem Statement:__ Did you know last year on the Redmon campus 11 million Microsoft compostable coffee cuts were used? How many of those do you think were appropriately composted? This brings our case in point: Recycling is necessary for a sustainable society, however with the mass production of items in various shapes, sizes, textures and materials, consumers (including I myself) often can get confused about how to determine the correct way of disposing of a large variety of materials. Therefore our problem is ubiquitous in the world: how can we solve the problem of humans having to segregate trash into the trash, compost and recycling without messing it up? Easy, we train a machine to help train humans. This is a human problem, which will take humans to fix, but using ML we can help humanity correct common misconceptions. 

__Objective:__ Build a system to help reinforce the Microsoft community on the best ways to reduce waste. In this project we will seek to categorize different pieces of waste into three categories: (1) Recyclable (2) Compost (3) Landfill using machine learning to identify and classify images for appropriate disposal. This will not only have a positive effect on the environment but also economical effects.

### Project Overview: Raspberry Pi Object Recognition and Classification for Waste
We’ll harness the power of some hardware, as well as a couple of APIs:

* Raspberry Pi B+ as our computer board of choice
* Raspberry Pi Camera Module
* OpenCV to enable accurate facial detection of photos
* Tensorflow
