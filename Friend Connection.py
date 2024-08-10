from collections import deque, defaultdict

class FriendNetwork:
    def __init__(self):

        # Space Complexity: O(V + E), where V is the number of people and E is the number of friendships.
        self.friends = defaultdict(set)
    
    def add_friendship(self, person1, person2):
    
        # Time Complexity: O(1) 
        self.friends[person1].add(person2)
        self.friends[person2].add(person1)
    
    def get_friends(self, person):

        # Time Complexity: O(1) for dictionary.
        return self.friends[person]
    
    def get_common_friends(self, person1, person2):
     
        # Time Complexity: O(min(f1, f2)), where f1 and f2 are the number of friends of person1 and person2 respectively.
        return self.friends[person1].intersection(self.friends[person2])
    
    def nth_connection(self, start, end):
      
        # Time Complexity: O(V + E), where V is the number of people and E is the number of friendships.
        # Space Complexity: O(V) 
        if start == end:
            return 0
        visited = set()
        queue = deque([(start, 0)])
        
        while queue:
            current_person, level = queue.popleft()
            visited.add(current_person)
            
            for friend in self.friends[current_person]:
                if friend == end:
                    return level + 1
                if friend not in visited:
                    queue.append((friend, level + 1))
        
        return -1

def main():
    network = FriendNetwork()
    
    # Example friendships
    network.add_friendship('Alice', 'Bob')
    network.add_friendship('Alice', 'Carol')
    network.add_friendship('Alice', 'Tom')
    network.add_friendship('Bob', 'Janice')
    network.add_friendship('Bob', 'Carol')
    network.add_friendship('Bob', 'Tom')
    network.add_friendship('Carol', 'Eve')
    network.add_friendship('Tom', 'Mark')
    
   
    print("Alice's Friends:", network.get_friends('Alice'))
    print("Bob's Friends:", network.get_friends('Bob'))
    
  
    common_friends = network.get_common_friends('Alice', 'Bob')
    print("Common Friends of Alice and Bob:", common_friends)
    
   
    connection_level = network.nth_connection('Alice', 'Janice')
    print("Connection Level between Alice and Janice:", connection_level)
    
    connection_level = network.nth_connection('Alice', 'Eve')
    print("Connection Level between Alice and Eve:", connection_level)
    
    connection_level = network.nth_connection('Alice', 'Mark')
    print("Connection Level between Alice and Mark:", connection_level)
    
    connection_level = network.nth_connection('Alice', 'Alice')
    print("Connection Level between Alice and Alice:", connection_level)
    
    connection_level = network.nth_connection('Alice', 'Frank')
    print("Connection Level between Alice and Frank:", connection_level)

if __name__ == "__main__":
    main()
