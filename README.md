
### Zero Shot Image Classification

#### simple test



#### Gradio Web Server

![zs_image_classification_clip.png](https://s2.loli.net/2024/02/22/oCuQG5FOBUf2iNE.png)

![zs_image_classification_clip2.png](https://s2.loli.net/2024/02/22/26AqDtVFGf9k5Qg.png)

#### CIFAR-10  experiment

- clip-vit-large-patch14

```
              precision    recall  f1-score   support

    airplane     0.9855    0.9490    0.9669      1000
  automobile     0.9728    0.9640    0.9684      1000
        bird     0.9034    0.9540    0.9280      1000
         cat     0.9158    0.9460    0.9306      1000
        deer     0.9319    0.9580    0.9448      1000
         dog     0.9578    0.9540    0.9559      1000
        frog     0.9943    0.8700    0.9280      1000
       horse     0.9454    0.9870    0.9658      1000
        ship     0.9807    0.9640    0.9723      1000
       truck     0.9554    0.9850    0.9700      1000

    accuracy                         0.9531     10000
   macro avg     0.9543    0.9531    0.9531     10000
weighted avg     0.9543    0.9531    0.9531     10000
```

- clip-vit-base-patch32

```
              precision    recall  f1-score   support

    airplane     0.9504    0.9010    0.9251      1000
  automobile     0.8785    0.9760    0.9247      1000
        bird     0.8124    0.8880    0.8485      1000
         cat     0.8190    0.8600    0.8390      1000
        deer     0.9341    0.7650    0.8411      1000
         dog     0.8508    0.8840    0.8671      1000
        frog     0.9699    0.7740    0.8610      1000
       horse     0.8127    0.9760    0.8869      1000
        ship     0.9446    0.9550    0.9498      1000
       truck     0.9688    0.9010    0.9337      1000

    accuracy                         0.8880     10000
   macro avg     0.8941    0.8880    0.8877     10000
weighted avg     0.8941    0.8880    0.8877     10000
```