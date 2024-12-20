{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNqhDHDrHMEF6WUydJ9OLkB",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AdarshaCoding/google_colab_practice/blob/main/test.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class Node:\n",
        "  def __init__(self, data) -> None:\n",
        "    self.data = data\n",
        "    self.next = None\n",
        "\n",
        "class SinglyLinkedList:\n",
        "  def __init__(self) -> None:\n",
        "    self.head = None\n",
        "\n",
        "  def append(self, data):\n",
        "    new_node = Node(data)\n",
        "    if self.head == None:\n",
        "      self.head = new_node\n",
        "      return\n",
        "\n",
        "    current = self.head\n",
        "    while current.next != None:\n",
        "      current = current.next\n",
        "    current.next = new_node\n",
        "\n",
        "  def print_list(self):\n",
        "    current = self.head\n",
        "    while current:\n",
        "      print(current.data, end=\" -> \")\n",
        "      current = current.next\n",
        "    print(\"None\")\n",
        "\n",
        " # 10 -> 20 -> 30 -> None\n",
        "  def reverse_list(self):\n",
        "    # keep adding all the nodes in reverse order to prev\n",
        "    prev = None\n",
        "    current = self.head\n",
        "    # travel till current == None\n",
        "    while current:\n",
        "      temp= current.next  # save current.next value : 20 ->30 -> None\n",
        "      current.next = prev # disconnecting the current link from the main list\n",
        "      prev = current   # keep the current version of List after disconnecting from the main\n",
        "      current = temp # update the current value for next iteration\n",
        "    self.head = prev  # finally update the head to prev\n",
        "\n"
      ],
      "metadata": {
        "id": "T3gdI2rDM6MH"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "ll = SinglyLinkedList()\n",
        "ll.append(10)\n",
        "ll.append(20)\n",
        "ll.append(30)\n",
        "ll.append(40)\n",
        "\n",
        "ll.print_list()\n",
        "ll.reverse_list()\n",
        "ll.print_list()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gnd9bVEjOCgs",
        "outputId": "4260d668-ef81-4d77-8f69-8fc779a3da35"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 -> 20 -> 30 -> 40 -> None\n",
            "40 -> 30 -> 20 -> 10 -> None\n"
          ]
        }
      ]
    }
  ]
}