#include <vector>
#include <algorithm>

float sigmaEff(vector<float> v, float threshold, float& xmin, float& xmax){
  
  std::sort(v.begin(),v.end());

  int total = v.size();
  int max = (int)(threshold * total);

  vector<float>  start;
  vector<float>  stop;
  vector<float>  width;
    
  unsigned i = 0 ;
  while (i != v.size()-1){
      
    int count = 0;
    unsigned j = i;
    while (j != v.size()-1 && count < max){
      
      ++count;
      ++j;

    }

    if ( j != v.size()-1){
      start.push_back(v[i]);
      stop .push_back(v[j]);
      width.push_back(v[j] - v[i]);
      
      //std::cout<<"xmin and xmax till now "<<start[i]<<" "<<stop[i]<<std::endl;
    }
    ++i;
  }
    
  float minwidth = *min_element(width.begin(), width.end());

  unsigned pos = min_element(width.begin(), width.end()) - width.begin();    

  xmin = start[pos];
  xmax = stop [pos];
  return minwidth;

}
