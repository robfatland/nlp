# Natural Language Processing on the public cloud

This tutorial covers building and running a Natural Language Processing (NLP) analysis on the cloud.


## Part 1: Preparation

- Set aside a couple hundred dollars (ideally in cloud credits) supporting a cloud account or subscription: AWS, Azure, GCP etcetera
- Learn about cloud security and cost management; follow best practices
    - Taking this on in earnest: One should plan on eight hours of "cloud 101" training to start with
    - Links here...
- Set up a modest Ubuntu Linux virtual machine on the cloud; and log in to that VM using **`ssh`**
- Update the machine: **`sudo apt-get update -y && sudo apt-get upgrade -y`**
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

* [YouTube link](https://youtu.be/xvqsFTUsOmc) for Alice Zhao's two-hour tutorial
* [GitHub link](https://github.com/adashofdata/nlp-in-python-tutorial.git)  
* These notes are from that lecture
* Natural language in this case will refer to language (the data) in text files
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
        * Clean the data to arrive at: the corpus and the document-term matrix (two data structures corresponding to the text)
        * Exploratory Data Analysis (EDA): word counts
        * NLP: As noted, sentiment analysis, topic modeling, text generation
    * Communication
        * Design: Scope, visualize, extract insights
        * Domain: Expertise 
* Data Science Workflow: Question / Data acquisition and cleaning / EDA / Apply technique(s) / Share insights
* Data acquisition and storage tools in Python
    * Python web scraping: Requests (gets everything), Beautiful Soup (pulls out just transcripts)
    * Saving Data: Pickle to serialize data for later use
* Data formats (cleaning)
    * Corpus is a collection of texts
        * pandas DataFrame to be used to store the corpus
            * Two columns: source identifier column and text column
                * Note entries in that second column are long strings of text
    * Document term matrix 
        * Clean text
            * using regex: remove punctuation, convert to all lower case, remove any terms that contain numbers
        * Tokenize text
            * break down into smaller parts: in this case by *word*: Every word is now an item.
            * remove stop words: they do not add much meaning
            * we are now in 'bow' bag of words format
        * Put the resulting words in matrix format
            * First column is source identifier
            * Subsequent columns are all possible tokens
            * matrix entries are number of occurrences of the token in that identified (row) source




