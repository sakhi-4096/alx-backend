# Caching 
A technique used in computer systems to store frequently accessed or recently used data in a smaller, faster memory space called a cache.

![Caching](https://media.makeameme.org/created/caching-t6vy7i.jpg)

## Description
The purpose of caching is to improve the overall performance of the system by reducing the time it takes to access data. Cache replacement policies are algorithms or strategies used by a cache memory system to decide which cache line to evict (remove) when a new data item needs to be brought into the cache and there is no space available. The goal of these policies is to maximize the effectiveness of the cache by keeping the most relevant and frequently used data in the cache, thereby reducing the number of cache misses.

## Features
* **Random Replacement:** This policy randomly selects a cache line for replacement. While simple, it doesn't consider the past behavior of the data's usage and may not be the most effective in terms of performance.
* **Least Recently Used (LRU):** LRU replacement policy replaces the cache line that has not been used for the longest period. This is often done using a counter or a linked list of recently accessed items. The downside is that it requires maintaining a record of the access history, which can be computationally expensive.
* **First-In-First-Out (FIFO):** In this policy, the cache line that has been in the cache the longest is replaced. This is typically implemented using a circular buffer or queue structure.
* **Least Frequently Used (LFU):** LFU replaces the cache line that has been used the least number of times. This requires maintaining a counter for each cache line to keep track of the usage frequency.
* **Most Recently Used (MRU):** MRU replaces the cache line that has been used most recently. This is the opposite of the LRU policy and, like LRU, requires maintaining access history.
* **Pseudo-LRU:** This is a compromise between LRU and simpler policies. It approximates LRU behavior without the need for a complete history by using a combination of counters or other mechanisms.
* **Optimal Replacement:** The optimal replacement policy, also known as the "oracle" policy, would replace the cache line that will not be used for the longest time in the future. However, it is impossible to implement in real systems because it requires knowledge of future access patterns.

## Credits
 * [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)
 * [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29)
 * [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29)
 * [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29)
 * [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29)

## Contact
 * [Twitter](https://www.twitter.com/sakhilelindah) / [Github](https://github.com/sakhi-4096) / [Mail](mailto:sakhilelindah@protonmail.com)
