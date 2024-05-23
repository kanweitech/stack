{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "355aab3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['A', 'B', 'C']\n",
      "C\n",
      "None\n",
      "3\n",
      "C\n"
     ]
    }
   ],
   "source": [
    "class Stack:\n",
    "    def __init__(self):\n",
    "        self.items = []\n",
    "    def push(self, item):\n",
    "        self.items.append(item)\n",
    "    def pop(self):\n",
    "        return self.items.pop()\n",
    "    def is_empty(self):\n",
    "        self.items == []\n",
    "    def size(self):\n",
    "        return len(self.items)\n",
    "    def peek(self):\n",
    "        return self.items[len(self.items) -1]\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    \n",
    "    s = Stack()\n",
    "    for i in [\"A\", \"B\", \"C\"]:\n",
    "        s.push(i)\n",
    "    print(s.items)\n",
    "    print(s.peek())\n",
    "    print(s.is_empty())\n",
    "    print(s.size())\n",
    "    print(s.pop())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b31907d",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
