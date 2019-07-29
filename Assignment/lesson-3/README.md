
### Question: 

1. 代码中66行生成数据集的时候，如果x是按序从小到大生成，lr就需要取很小才能使loss减小，否则会到很大，为什么会这样?

```
def gen_sample_data():
    w = random.randint(0, 10) + random.random()  # for noise random.random[0, 1)
    b = random.randint(0, 5) + random.random()
    num_samples = 100
    x_list = []
    y_list = []
    for i in range(num_samples):
        x = i #random.randint(0, 100) * random.random() #这里有序了之后，学习率需要取很小才可以？
        y = w * x + b + random.random() * random.randint(-1, 1)
        x_list.append(x)
        y_list.append(y)
    return x_list, y_list, w, b
```


