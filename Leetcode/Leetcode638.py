class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        memo=dict()

        def dfs(nds):
            if tuple(nds) in memo:
                return memo[tuple(nds)]

            # set default price
            cost=0
            for p,n in zip(price,nds):
                cost+=p*n

            for offer in special:
                status=True
                for nn,oo in zip(nds,offer):
                    if nn<oo:
                        status=False
                        break 
                if status:
                    newNds=[n-offer[i] for i, n in enumerate(nds)]
                    cost=min(cost,offer[-1]+dfs(tuple(newNds)))

            memo[tuple(nds)]=cost #memoization
            return cost


        return dfs(tuple(needs))
