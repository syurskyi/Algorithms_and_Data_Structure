c_ Solution
    ___ solution candidates,ans,cur,target,index,sum
        __(sum__target
            ans.a..(cur[:])
        ____(sum<target
            n _ l..(candidates)
            ___ i __ r..(index,n
                ?.a..(candidates[i])
                solution(candidates,ans,cur,target,i,sum+candidates[i])
                ?.p.. 
        r_
    ___ combinationSum candidates: List[i..], target: i..) __ List[List[i..]]:
        ans _    # list
        cur _    # list
        solution(candidates,ans,cur,target,0,0)
        r_ ans