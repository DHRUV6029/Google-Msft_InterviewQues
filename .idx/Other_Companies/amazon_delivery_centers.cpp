int suitableLocation(vector<int> center, long d) {
    
    // helper function to get the total distance
    auto getTotalDist = [&center](int mid) {
        long total = 0;
        for (int ii = 0; ii < center.size(); ++ii) {
            total += 2 * abs(center[ii] - mid);
        }
        return total;
    };

    // find the lowest point that is suitable
    int lo = -1e9, hi = 1e9;
    bool found = false;
    int first = -1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        long dist = getTotalDist(mid);
        long dist1 = getTotalDist(mid+1);
        
        if (dist <= d) {
            found = true;
            first = mid;
            hi = mid - 1;
        } else if (dist < dist1) {
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    
    if (!found) return 0;
    
    // find the highest point that is suitable
    lo = first, hi = 1e9;
    int last = -1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        long dist = getTotalDist(mid);
        long dist1 = getTotalDist(mid+1);
        
        if (dist <= d) {
            last = mid;
            lo = mid + 1;
        } else if (dist < dist1) {
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    
    return last - first + 1;
}
