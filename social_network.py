# social_network.py

# -----------------------------
# Person Class
# -----------------------------
class Person:
    def __init__(self, name):
        """Initialize a person with a name and an empty list of friends."""
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        """Add a friend (Person object) to the person's friends list if not already added."""
        if friend not in self.friends:
            self.friends.append(friend)


# -----------------------------
# SocialNetwork Class
# -----------------------------
class SocialNetwork:
    def __init__(self):
        """Initialize the social network with an empty dictionary of people."""
        self.people = {}

    def add_person(self, name):
        """Add a new person to the network if they don't already exist."""
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} already exists in the network.")

    def add_friendship(self, person1_name, person2_name):
        """Establish a bidirectional friendship between two people."""
        if person1_name not in self.people or person2_name not in self.people:
            print(f"Friendship not created. One or both users don't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        # Add each person to the other's friends list
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        """Print the entire social network with each person's friends."""
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names) if friend_names else 'No friends yet.'}")


# -----------------------------
# Test the Social Network
# -----------------------------
if __name__ == "__main__":
    network = SocialNetwork()

    # Add people
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    # Create friendships
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Jordan", "Johnny")  # Johnny doesn't exist
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    # Print the network
    print("\n--- Social Network ---")
    network.print_network()


# -------------------------------------------------------
# DESIGN MEMO (200–300 Words)
# -------------------------------------------------------
"""
Design Memo: Social Network Graph

A graph is the ideal data structure to represent a social network because it naturally models relationships as
connections (edges) between users (nodes). In this system, each Person acts as a node, and friendships represent
edges connecting those nodes. Unlike a list or a tree, graphs allow for flexible, bidirectional relationships where
connections can form in any pattern—circles of friends, mutual links, and large interconnected communities.

Lists would limit the representation to linear connections, and trees would enforce a hierarchical structure with
one-way relationships. In contrast, real-world social networks are non-hierarchical and highly interconnected, with
people forming complex, overlapping groups. Graphs efficiently handle these dynamic and mutual relationships, allowing
for features like friend recommendations, shortest-path calculations (degrees of separation), and community detection.

In terms of performance trade-offs, adding people is straightforward with O(1) time complexity since we use a dictionary
for quick lookups. Adding friendships requires O(1) operations as well because we directly reference existing Person
instances. However, printing the entire network becomes O(n + m), where n is the number of people and m is the number
of connections—this grows as the network expands.

Overall, the graph model provides scalability, flexibility, and realism in representing social systems, making it the
best structure for this application.
"""
