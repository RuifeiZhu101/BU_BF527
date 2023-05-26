{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "91ab4c9d-ac77-469a-92f0-49bc7ce7c92b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# python template code for exercise ID DNA (Counting DNA Nucleotides)\n",
    "# your code *must* define a function called run to work\n",
    "    \n",
    "file = open(\"rosalind_dna.txt\")\n",
    "dna = file.readlines()\n",
    "s =''\n",
    "for ele in dna:\n",
    "    s=ele\n",
    "\n",
    "def run(s):\n",
    "  # use the print() function to print out counts of A, C, G, and T in s on one\n",
    "  # line separated by spaces\n",
    "\n",
    "    #initialize variables to store the counts of A, C, G, and T\n",
    "    n_A=0\n",
    "    n_C=0\n",
    "    n_G=0\n",
    "    n_T=0\n",
    "    for i in s:\n",
    "        if i==\"A\":\n",
    "            n_A+=1\n",
    "        elif i==\"C\":\n",
    "            n_C+=1\n",
    "        elif i==\"G\":\n",
    "            n_G+=1\n",
    "        elif i==\"T\":\n",
    "            n_T+=1\n",
    "    print(n_A,n_C,n_G,n_T)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "79e42e6a-9688-4bbb-9d83-400499dfbc31",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "196 218 210 201\n"
     ]
    }
   ],
   "source": [
    "run(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6fee5db7-851c-4936-905e-cb904237e311",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c6b02a9-0889-4161-bfbf-3871ee82a587",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
