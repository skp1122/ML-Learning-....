{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# save this funtioin as python module \"clean_text\"\n",
    "\n",
    "from nltk.tokenize import RegexpTokenizer\n",
    "from nltk.stem.porter import PorterStemmer\n",
    "from nltk.corpus import stopwords\n",
    "import sys\n",
    "\n",
    "\n",
    "# Init objects\n",
    "tokenizer = RegexpTokenizer(r'\\w+')\n",
    "en_stopwords = set(stopwords.words('english'))\n",
    "ps = PorterStemmer()\n",
    "\n",
    "def getCleanedReview(review):\n",
    "    \n",
    "    review = review.lower()\n",
    "    review = review.replace(\"<br /><br />\",\" \")\n",
    "    \n",
    "    # Tokenize\n",
    "    tokens = tokenizer.tokenize(review)\n",
    "    new_tokens = [token for token in tokens if token not in en_stopwords]\n",
    "    stemmed_tokens = [ps.stem(token) for token in new_tokens]\n",
    "    \n",
    "    cleaned_review = ' '.join(stemmed_tokens)\n",
    "    return cleaned_review\n"
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
