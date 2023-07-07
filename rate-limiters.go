package main

type RateLimiter struct {
	queue ConcurrentQueue
}

func (r *RateLimiter) tokenBucket(size int, refillRate int) bool {

	return true
}

func (r *RateLimiter) leakingBucket() bool {

	return true
}

func (r *RateLimiter) fixedWindowCounter() bool {
	return true
}

func (r *RateLimiter) slidingWindowLog() bool {
	return true
}

func (r *RateLimiter) slidingWindowCounter() bool {
	return true
}
