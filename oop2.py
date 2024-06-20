class Watu:
    def __init__(self, jina, miaka):
        self.jina = jina
        self.miaka = miaka

    def kuonyesha(self):
        print(self.jina, self.miaka)


my_data = Watu("Siso", "56")
my_data.kuonyesha()
my_data1 = Watu("Jack", "76")
my_data1.kuonyesha()
my_data2 = Watu("Bruno", "55")
my_data2.kuonyesha()
my_data3 = Watu("Caro", "65")
my_data3.kuonyesha()
my_data4 = Watu("Anne", "20")
my_data4.kuonyesha()
