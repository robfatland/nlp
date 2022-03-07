# Natural Language Processing on the public cloud

This tutorial covers building and running a Natural Language Processing (NLP) analysis on the cloud.


## Part 1: Preparation

- Set aside a couple hundred dollars (ideally in cloud credits) supporting a cloud account or subscription: AWS, Azure, GCP etcetera
- Learn about cloud security and cost management; follow best practices
    - Taking this on in earnest: One should plan on eight hours of "cloud 101" training to start with
    - Links here...
- Set up a modest Ubuntu Linux virtual machine on the cloud; and log in to that VM using **`ssh`**
- On that machine: Install Python and a Jupyter notebook server (for example Anaconda or Miniconda)
- Clone [this repository](https://github.com/robfatland/nlp)
- Clone [Alice Zhao's Python NLP tutorial repository](https://github.com/adashofdata/nlp-in-python-tutorial.git)
- Use the **`conda`** package manager to install three NLP libraries
    * **`conda install -c conda-forge wordcloud`** and confirm with **`y`**
    * **`conda install -c conda-forge textblob`** and **`y`** to confirm
    * **`conda install -c conda-forge gensim`** and **`y`** to confirm


## Part 2: Natural Language Processing

- Start your Jupyter notebook server and test the Hello World notebook in the Alice Zhao tutorial repository
    - To keep that tutorial distinct from this one: I will refer to is as the AZ tutorial
    - Use the AZ tutorial first and foremost: It is already a well-developed learning experience
    - If you want to go further: Explore the material in this tutorial





## Notes from Alice Zhao's Tutorial

* [YouTube link](https://youtu.be/xvqsFTUsOmc) for a two-hour tutorial
* [GitHub link](https://github.com/adashofdata), particularly 
* These notes are taken directly from that lecture
* Sentiment analysis introduced: Distillation of collective sentiment from a sea of words
* Topic modeling introduced: How many topics live in your Inbox?
* Text generation introduced: Creating text that perhaps makes sense
* Data science: Using data to make decisions; getting meaning from text...
    * Andrew Conway's Euler diagram: Data scientists have all three skills: Programming, Math/Stats and Communication skills
    * Low on the communication skills? Ok more a Developer
    * Programming skills and Communication skills (but no math)? Danger zone! Throw tools and libraries at the data and hope...
* Breakdown of NLP in Python
    * Programming: 
        * For Data: pandas, sklearn, re (regular expressions)
        * NLP: nltk, TextBlob, gensim
    * Math, Statistics
        * Clean the data to arrive at: the corpus and the document-term matrix
        * Exploratory Data Analysis (EDA): word counts
        * NLP: As noted, sentiment analysis, topic modeling, text generation
    * Communication
        * Design: Scope, visualize, extract insights
        * Domain: Expertise 
* Data Science Workflow
    * Start with a question
    * Get, clean data
    * EDA
    * Apply some technique
    * Share insights


