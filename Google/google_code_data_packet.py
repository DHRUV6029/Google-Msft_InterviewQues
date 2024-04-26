def min_packages(total_data, package_limit):
    dp = [float('inf')] * (total_data + 1)
    dp[0] = 0
    
    for i in range(1, total_data + 1):
        for j in range(1, min(i, package_limit) + 1):
            dp[i] = min(dp[i], dp[i - j] + 1)
    
    return dp[total_data]

# Example usage:
total_data = 30
package_limit = 9
split_points = {5, 8}  
print("Minimum number of packages:", min_packages(total_data, package_limit))
def min_packages_with_split_points(total_data, package_limit, split_points):
    dp = [float('inf')] * (total_data + 1)
    dp[0] = 0
    
    for i in range(1, total_data + 1):
        for j in range(1, min(i, package_limit) + 1):
            if i - j in split_points:
                dp[i] = min(dp[i], dp[i - j] + 1)
    
    return dp[total_data]

# Example usage:
total_data = 12
package_limit = 6
split_points = {5, 8}  # Allowed split points at index 5 and 8
print("Minimum number of packages with split points:", min_packages_with_split_points(total_data, package_limit, split_points))


