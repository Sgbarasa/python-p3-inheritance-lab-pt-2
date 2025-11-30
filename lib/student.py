#!/usr/bin/env python3

class Student:
    """Represents a student."""

    def __init__(self):
        self.knowledge = []

    def hello(self):
        """Says a brief greeting."""
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        """Respectfully tries to get the teacher's attention."""
        print("Pick me!")


class ChattyStudent(Student):
    """A chatty student that talks a lot."""

    def hello(self):
        """Says a greeting, then chatty commentary."""
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        """Raises hand ten times to get attention."""
        for _ in range(10):
            print("Pick me!")
