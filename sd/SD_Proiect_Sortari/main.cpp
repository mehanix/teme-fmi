#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>
#include <chrono>
#include <algorithm>
#define M_OF_3 1
#define LAST_ELEM 0
using namespace std;

ifstream fin("test.in");
ofstream fout("a.out");

void generate_random(vector<int>& input, const int nr_elem, const int val_max) {

    input.clear();
    for (int i=0;i<nr_elem;i++) {
        input.push_back((1+rand())%val_max);
    }

}

string bubble_sort(vector<int>& v, int n) {
    if (n>99999)
        return "ERROR: too many elements";
    int ok=0;
    while(ok==0){
    ok=1;
    for(int i=0;i<n-1;i++)
        if(v[i]>v[i+1]) {
                iter_swap(v.begin()+i, v.begin()+i+1);
                ok=0;
        }
    }
    return "OK";
}

bool isSorted(vector<int> v,int n) {

    for(int i=0;i<n-1;i++)
        if (v[i] > v[i+1])
            return false;
    return true;
}

/// swaps 2 values in a vector, index-based
void swap_val(vector<int>&v, int i, int j){

    int aux = v[i];
    v[i] = v[j];
    v[j] = aux;
}

int median_of_3(vector<int>&v, int left, int right) {

    ///calculez pivot, mediana din 3
    int mid = (left+right)/2;

    ///pun in ordine
    if (v[left] > v[mid])
        swap_val(v,left,mid);
    if(v[left] > v[right])
        swap_val(v,left,right);
    if (v[mid] > v[right])
        swap_val(v,mid,right);
    return mid;

}

pair<int,int> partitionn(vector<int>&v, int left, int right,int mid){


    //cout<<v[left]<<' '<<v[mid]<<' '<<v[right]<<'\n';

    ///partitionez cu algoritmul lui Lomuto modificat
    int pivot = v[mid];
    swap_val(v,mid,right);
    /// left [ mai mici strict ) l [egale) r [ neverificate ] u ( mai mari ] right
    int l = left;
    int r = left;
    int u = right;
    while (r<=u) {
        if(v[r] < pivot){
        swap_val(v,l,r);
        l=l+1;
        r=r+1;
        }
        else if (v[r] > pivot) {
            swap_val(v,r,u);
            u=u-1;
        }
        else
            r=r+1;
    }
    return make_pair(l,r);



}

void quick_sort_util(vector<int>& v, int left, int right, bool mode) {

    if (left < right){
    int mid;
    if (mode == M_OF_3)
        mid = median_of_3(v,left,right);
        else
        mid = right;
    pair<int,int> q = partitionn(v,left,right,mid);


    quick_sort_util(v,left,q.first-1,mode);
    quick_sort_util(v,q.second,right,mode);
    }



}
///fct wrapper pt error handling
string quick_sort(vector<int>&v, int left, int right,bool mode){

    quick_sort_util(v,left,right,mode);
    return "OK";
}


string count_sort(vector<int>&v,int nr_elem,int val_max){

    if (val_max >= 1000000)
        return "ERROR: numbers too large to sort using Count Sort";

    vector<int> cnt(val_max+1, 0);

    for(auto &i:v)
        cnt[i]++;

    int x=0;
    for(int j=0;j<cnt.size();j++)
        while(cnt[j]--!=0)
            v[x++]=j;

    return "OK";
}

void merge(vector<int> &v,int l,int m,int r){


    //copie [l,m](m,r]

    int i,j,k;

    //int n1 = m - l + 1;
    //int n2 = r - m;
    vector<int> c(r-l+1);

    /*
    for(int x=0;x<n1;x++)
        L[x] = v[l+x];

    for(int x=0;x<n2;x++)
        R[x]=v[m+1+x];*/

    i=l;
    j=m+1;
    k=0;

    ///interclasare
    while(i <= m && j <= r) {

        if(v[i]<=v[j])
            c[k]=v[i++];
        else
            c[k]=v[j++];
        k++;
    }

    while(i<=m)
        c[k++]=v[i++];

    while(j<=r)
        c[k++]=v[j++];

    //for(auto &i:c)
    //    cout<<i<<' ';
    //cout<<'\n';

    for (i = l, k = 0; i <= r; i++, k++)
        v[i] = c[k];
    c.clear();

}

string merge_sort(vector<int> &v, int l, int r) {

    if (l < r) {

        int m = l+(r-l)/2;
        merge_sort(v,l,m);
        merge_sort(v,m+1,r);

        merge(v,l,m,r);
    }
    return "OK";
}

void count_sort_radix(vector<int>& v, int n, int exp,int radix) {
    vector<int> output(n);
    vector<int> cnt(radix,0);
    ///numara dupa cifra curenta
    for(auto &x:v)
        cnt[(x/exp)%radix]++;

    ///reconstruieste vectorul
    for (int i=1;i<radix;i++)
        cnt[i]+=cnt[i-1];

    int d;
    for(int i=n-1;i>=0;i--) {
        d = (v[i]/exp)%radix;
        output[cnt[d]-1] = v[i];
        cnt[d]--;
    }

    v = output;

}

int get_max(vector<int>& v){
int x=-1;
    for(auto &i:v)
        if(x<i)
            x=i;
return x;
}
string radix_sort(vector<int>& v,int nr_elem, int val_max, int radix){

    int maxx = get_max(v);
    for (unsigned long long exp=1; maxx/exp > 0; exp*=radix) {
        count_sort_radix(v,nr_elem,exp,radix);
    }

    return "OK";
}

int main()
{
    std::srand(std::time(nullptr));
    vector<int> v;
    int nr_tests, nr_elem, val_max;
    //citesc test data
    fin>>nr_tests;
    string result;
    for(int i=0;i<nr_tests;i++) {

        fin>>nr_elem>>val_max;
        cout<<"TEST "<<i<<" ======== NR ELEM: "<<nr_elem<<" ======= VAL MAX: "<<val_max<<"\n";
        cout<<"Generez elementele -------------- ";
        generate_random(v,nr_elem,val_max);
        cout<<"Done!\n";



        cout<<"STL sort --------- SUCCESS ------ ";
        vector<int> v_copy = v;
        auto begin = chrono::steady_clock::now();
        sort(v_copy.begin(), v_copy.end());
        auto end = chrono::steady_clock::now();
        auto eta = chrono::duration_cast<chrono::milliseconds>(end - begin).count();
        cout<<eta<<"ms\n";


        cout<<"Bubble sort ------ ";
        v_copy = v;
        begin = chrono::steady_clock::now();
        result = bubble_sort(v_copy,nr_elem);
        end = chrono::steady_clock::now();
        eta = chrono::duration_cast<chrono::milliseconds>(end - begin).count();
        if(result.compare("OK") == 0) {
            if (isSorted(v_copy,nr_elem) == true)
                cout<<"SUCCESS ------ "<<eta<<"ms\n";
        }
        else
            cout<<result<<"\n";

        cout<<"Quick sort ------- ";
        v_copy = v;
        begin = chrono::steady_clock::now();

        result = quick_sort(v_copy,0,nr_elem-1,M_OF_3);

        end = chrono::steady_clock::now();
        eta = chrono::duration_cast<chrono::milliseconds>(end - begin).count();
        if(result.compare("OK") == 0) {
            if (isSorted(v_copy,nr_elem) == true)
                cout<<"SUCCESS ------ "<<eta<<"ms ----- (median of three)\n";
        }
        else
            cout<<result<<"\n";

        cout<<"Quick sort ------- ";
        v_copy = v;
        begin = chrono::steady_clock::now();
        result = quick_sort(v_copy,0,nr_elem-1,LAST_ELEM);
        end = chrono::steady_clock::now();
        eta = chrono::duration_cast<chrono::milliseconds>(end - begin).count();
        if(result.compare("OK") == 0) {
            if (isSorted(v_copy,nr_elem) == true)
                cout<<"SUCCESS ------ "<<eta<<"ms ----- (pivot always last element)\n";
        }
        else
            cout<<result<<"\n";

        cout<<"Count sort ------- ";
        v_copy = v;
        begin = chrono::steady_clock::now();
        result = count_sort(v_copy,nr_elem,val_max);
        end = chrono::steady_clock::now();
        eta = chrono::duration_cast<chrono::milliseconds>(end - begin).count();
        if(result.compare("OK") == 0) {
            if (isSorted(v_copy,nr_elem) == true)
                cout<<"SUCCESS ------ "<<eta<<"ms\n";
                else
                cout<<"ERROR: Bad sort "<<" \n";
        }
        else
            cout<<result<<"\n";

        cout<<"Merge sort ------- ";
        v_copy = v;
        begin = chrono::steady_clock::now();
        result = merge_sort(v_copy,0,nr_elem-1);
        end = chrono::steady_clock::now();
        eta = chrono::duration_cast<chrono::milliseconds>(end - begin).count();
        if(result.compare("OK") == 0) {
            if (isSorted(v_copy,nr_elem) == true)
                cout<<"SUCCESS ------ "<<eta<<"ms\n";
                else
                {
                cout<<eta<<"ERROR: Bad sort\n";
                    for(auto &i:v_copy)
                        cout<<i<<' ';

                }
        }
        else
            cout<<result<<"\n";

        cout<<"Radix sort ------- ";
        v_copy = v;
        begin = chrono::steady_clock::now();
        result = radix_sort(v_copy,nr_elem,val_max,10);
        end = chrono::steady_clock::now();
        eta = chrono::duration_cast<chrono::milliseconds>(end - begin).count();
        if(result.compare("OK") == 0) {
            if (isSorted(v_copy,nr_elem) == true)
                cout<<"SUCCESS ------ "<<eta<<"ms ----- (Base 10)\n";
                else
                {
                    cout<<"ERROR: Bad sort\n";
                    for(auto &i:v_copy)
                        cout<<i<<' ';

                }
        }
        else
            cout<<result<<"\n";



        cout<<"Radix sort ------- ";
        v_copy = v;
        begin = chrono::steady_clock::now();
        result = radix_sort(v_copy,nr_elem,val_max,256);
        end = chrono::steady_clock::now();
        eta = chrono::duration_cast<chrono::milliseconds>(end - begin).count();
        if(result.compare("OK") == 0) {
            if (isSorted(v_copy,nr_elem) == true)
                cout<<"SUCCESS ------ "<<eta<<"ms ----- (Base 256)\n";

                else
                {
                    cout<<"ERROR: Bad sort\n";
                    for(auto &i:v_copy)
                        cout<<i<<' ';

                }        }
        else
            cout<<result<<"\n";

        cout<<"\n\n";
    }
    return 0;
}
