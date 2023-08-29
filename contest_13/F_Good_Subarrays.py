def solve(a,n):
    #1 2 0
    #prefix_sum = [0,1,3,3]
    #[1,2,4,4]
    count = 0
    prefix_sum = [0] * (n+1)
    prefix_sum[0] = a[0]
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + a[i]
  
    occurrences = {}
    print(prefix_sum)
    for i in range(n+1):
        diff = prefix_sum[i] - i
        count += occurrences.get(diff, 0)
        occurrences[diff] = occurrences.get(diff, 0) + 1
    print(count)

    #1 2 0
    """
    #include <bits/stdc++.h>
using namespace std;
#define ll long long 
#define mod 1000000007
#define endl ("\n")
#define pi (3.141592653589)
#define mod 1e9+7
//#define int long long
#define float double
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define all(c) c.begin(), c.end()
#define min3(a, b, c) min(c, min(a, b))
#define min4(a, b, c, d) min(d, min(c, min(a, b)))
#define rrep(i, n) for(int i=n-1;i>=0;i--)
#define rep(i,n) for(int i=0;i<n;i++)


int main(){
    int t;
    cin>>t;
    while(t--){
    	int n;
    	cin>>n;
    	string s;
    	cin>>s;
    	vector<int> a(n);
    	rep(i, n) a[i] = s[i] - '0' - 1;
    	map<int, ll> mm;
    	ll ans = 0;
    	mm[0] = 1;
    	ll r = 0;
    	rep(i, n)
    	{
        	r += a[i];
        	ans += mm[r];
        	mm[r]++;
    	}
    	cout << ans <<endl;
	}
}
    """



















        
            

t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    arr = [int(x) for x in a]
    solve(arr,n)