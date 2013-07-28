#ifndef TREE_H_
#define TREE_H_
struct node{
  int v;
  struct node* left;
  struct node* right;
};

struct node* create_sample_tree();
struct node* create_tree_from_array();

#endif
