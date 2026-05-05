{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO+a2c6wvDGCkeootqA4C1T",
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
        "<a href=\"https://colab.research.google.com/github/kusuma-gowda446/DSA-using-python/blob/main/substrings2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Assignment 4:\n",
        "Given two strings s and p, the task is to find the smallest substring in s that contains all characters of p, including duplicates. If no such substring exists, return \"\". If multiple substrings of the same length are found, return the one with the smallest starting index.\n",
        "\n",
        "Examples:\n",
        "\n",
        "Input: s = \"timetopractice\", p = \"toc\"\n",
        "Output: toprac\n",
        "Explanation: \"toprac\" is the smallest substring in which \"toc\" can be found.\n",
        "\n",
        "Input: s = \"zoomlazapzo\", p = \"oza\"\n",
        "Output: apzo\n",
        "Explanation: \"apzo\" is the smallest substring in which \"oza\" can be found."
      ],
      "metadata": {
        "id": "F1hA0titYtIX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from collections import Counter\n",
        "def smallest(s,p):\n",
        "    if not s or not p :\n",
        "        return \"\"\n",
        "    need=Counter(p)  # length of the p unique elements\n",
        "    have={}    # dictories for present values\n",
        "    formed=0    # checking if the requirement is matching\n",
        "    required=len(need)   # length of the need variable\n",
        "    left=0    # left pointer\n",
        "    min_len=float(\"inf\")    # assigning min_substring value to +ve infinity\n",
        "    result=\"\"     # resulting variable\n",
        "\n",
        "    for right in range(len(s)):\n",
        "        char=s[right]\n",
        "        have[char]=have.get(char,0)+1\n",
        "\n",
        "        if char in need and need[char]==have[char]:\n",
        "            formed+=1\n",
        "\n",
        "        while formed==required:  #timetopractice\n",
        "            window_len=right-left+1\n",
        "\n",
        "            if window_len<min_len:\n",
        "                min_len=window_len\n",
        "                result=s[left:right+1]\n",
        "\n",
        "            left_char=s[left]\n",
        "            have[left_char]-=1\n",
        "            if left_char in need and have[left_char]<need[left_char]:\n",
        "                formed-=1\n",
        "\n",
        "            left+=1\n",
        "    return result\n",
        "\n",
        "s=\"timetopractice\"\n",
        "p=\"toc\"\n",
        "smallest(s,p)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "aUU3hDb2YuAs",
        "outputId": "127df1fa-c987-4dcd-f58c-fb6b6c34e25c"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'toprac'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 1
        }
      ]
    }
  ]
}