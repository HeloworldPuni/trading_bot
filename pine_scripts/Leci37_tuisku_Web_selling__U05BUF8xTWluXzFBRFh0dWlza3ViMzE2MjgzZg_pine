//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: ADX_and_DI
// ID_model: SNAP_1Min_1ADX_b316283f Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SNAP_1Min_1ADX_b316283f", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SNAP_1Min_b316283f(dx, diMinus, directionalMovementMinus, adx, diPlus, directionalMovementPlus, smoothedTrueRange, smoothedDirectionalMovementPlus, smoothedDirectionalMovementMinus, trueRange)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( diMinus <= 43.9974 )
		if( diPlus <= 48.0442 )
			if( smoothedTrueRange <= 0.030206 )
				if( directionalMovementPlus <= 7.4e-05 )
					if( directionalMovementMinus <= 0.015007 )
						if( diPlus <= 45.7945 )
							if( trueRange <= 0.01 )
								if( directionalMovementPlus <= 6.5e-05 )
									ret := -0.005338
								if( directionalMovementPlus > 6.5e-05 )
									ret := 0.913043 // buy
							if( trueRange > 0.01 )
								if( diPlus <= 2.61255 )
									ret := 0.237374
								if( diPlus > 2.61255 )
									ret := 0.042974
						if( diPlus > 45.7945 )
							if( smoothedTrueRange <= 0.026499 )
								if( trueRange <= 0.010102 )
									ret := 0.191489
								if( trueRange > 0.010102 )
									ret := 0.710843 // buy
							if( smoothedTrueRange > 0.026499 )
								ret := -0.444444
					if( directionalMovementMinus > 0.015007 )
						if( diMinus <= 30.3233 )
							if( smoothedTrueRange <= 0.013646 )
								if( smoothedTrueRange <= 0.013343 )
									ret := -0.227273
								if( smoothedTrueRange > 0.013343 )
									ret := -0.541667
							if( smoothedTrueRange > 0.013646 )
								if( smoothedDirectionalMovementMinus <= 0.001587 )
									ret := 0.739130 // buy
								if( smoothedDirectionalMovementMinus > 0.001587 )
									ret := 0.070363
						if( diMinus > 30.3233 )
							if( diPlus <= 31.3403 )
								if( trueRange <= 0.039373 )
									ret := 0.065984
								if( trueRange > 0.039373 )
									ret := 0.247839
							if( diPlus > 31.3403 )
								if( smoothedDirectionalMovementPlus <= 0.008627 )
									ret := 0.399267
								if( smoothedDirectionalMovementPlus > 0.008627 )
									ret := 0.704545 // buy
				if( directionalMovementPlus > 7.4e-05 )
					if( adx <= 27.7732 )
						if( directionalMovementMinus <= 0.002532 )
							if( diMinus <= 25.529 )
								if( dx <= 4.99406 )
									ret := 0.140162
								if( dx > 4.99406 )
									ret := 0.016808
							if( diMinus > 25.529 )
								if( smoothedTrueRange <= 0.016336 )
									ret := -0.001393
								if( smoothedTrueRange > 0.016336 )
									ret := -0.215105
						if( directionalMovementMinus > 0.002532 )
							if( directionalMovementPlus <= 0.004199 )
								if( diPlus <= 12.9765 )
									ret := -0.493976
								if( diPlus > 12.9765 )
									ret := 0.157754
							if( directionalMovementPlus > 0.004199 )
								if( trueRange <= 0.022092 )
									ret := 0.379032
								if( trueRange > 0.022092 )
									ret := 0.130261
					if( adx > 27.7732 )
						if( diPlus <= 23.6473 )
							if( smoothedDirectionalMovementPlus <= 0.004261 )
								if( smoothedDirectionalMovementMinus <= 0.000413 )
									ret := 0.482353
								if( smoothedDirectionalMovementMinus > 0.000413 )
									ret := -0.055838
							if( smoothedDirectionalMovementPlus > 0.004261 )
								if( diMinus <= 12.7287 )
									ret := -0.173228
								if( diMinus > 12.7287 )
									ret := 0.128088
						if( diPlus > 23.6473 )
							if( diMinus <= 16.2349 )
								if( diMinus <= 6.58917 )
									ret := -0.128739
								if( diMinus > 6.58917 )
									ret := 0.002298
							if( diMinus > 16.2349 )
								if( diPlus <= 24.4627 )
									ret := -0.503356
								if( diPlus > 24.4627 )
									ret := -0.208850
			if( smoothedTrueRange > 0.030206 )
				if( adx <= 93.1332 )
					if( diMinus <= 2.36595 )
						if( dx <= 92.7152 )
							if( smoothedDirectionalMovementMinus <= 0.000668 )
								ret := 0.111111
							if( smoothedDirectionalMovementMinus > 0.000668 )
								if( dx <= 88.1847 )
									ret := 0.285714
								if( dx > 88.1847 )
									ret := 0.892157 // buy
						if( dx > 92.7152 )
							if( smoothedDirectionalMovementPlus <= 0.014061 )
								ret := -0.944444 // sell
							if( smoothedDirectionalMovementPlus > 0.014061 )
								if( directionalMovementPlus <= 0.000662 )
									ret := 0.812500 // buy
								if( directionalMovementPlus > 0.000662 )
									ret := 0.220000
					if( diMinus > 2.36595 )
						if( dx <= 15.37 )
							if( diPlus <= 13.2455 )
								if( diPlus <= 12.8424 )
									ret := -0.226190
								if( diPlus > 12.8424 )
									ret := -0.862069 // sell
							if( diPlus > 13.2455 )
								if( dx <= 10.4405 )
									ret := -0.006258
								if( dx > 10.4405 )
									ret := 0.112455
						if( dx > 15.37 )
							if( directionalMovementMinus <= 0.006594 )
								if( smoothedTrueRange <= 0.0678 )
									ret := -0.144041
								if( smoothedTrueRange > 0.0678 )
									ret := 0.018981
							if( directionalMovementMinus > 0.006594 )
								if( diPlus <= 7.23777 )
									ret := -0.237778
								if( diPlus > 7.23777 )
									ret := -0.012912
				if( adx > 93.1332 )
					if( smoothedTrueRange <= 0.050349 )
						ret := 0.777778 // buy
					if( smoothedTrueRange > 0.050349 )
						ret := 1.000000 // buy
		if( diPlus > 48.0442 )
			if( trueRange <= 0.011511 )
				if( directionalMovementPlus <= 1.7e-05 )
					if( smoothedDirectionalMovementMinus <= 0.000749 )
						if( diPlus <= 78.3472 )
							if( dx <= 52.8401 )
								ret := -0.363636
							if( dx > 52.8401 )
								if( diPlus <= 50.3369 )
									ret := 0.076923
								if( diPlus > 50.3369 )
									ret := -0.191489
						if( diPlus > 78.3472 )
							if( adx <= 43.7105 )
								if( adx <= 37.4189 )
									ret := -0.444444
								if( adx > 37.4189 )
									ret := -0.846154 // sell
							if( adx > 43.7105 )
								ret := -0.333333
					if( smoothedDirectionalMovementMinus > 0.000749 )
						if( diMinus <= 37.8425 )
							if( diPlus <= 66.556 )
								if( diMinus <= 12.778 )
									ret := -0.306452
								if( diMinus > 12.778 )
									ret := 0.173572
							if( diPlus > 66.556 )
								if( smoothedTrueRange <= 0.030718 )
									ret := -0.167464
								if( smoothedTrueRange > 0.030718 )
									ret := 0.692308
						if( diMinus > 37.8425 )
							if( adx <= 45.609 )
								if( smoothedDirectionalMovementMinus <= 0.00145 )
									ret := 0.285714
								if( smoothedDirectionalMovementMinus > 0.00145 )
									ret := -0.206799
							if( adx > 45.609 )
								ret := 0.590909
				if( directionalMovementPlus > 1.7e-05 )
					if( diPlus <= 49.9855 )
						if( trueRange <= 0.009958 )
							if( smoothedDirectionalMovementMinus <= 0.004528 )
								if( diMinus <= 41.5189 )
									ret := -0.384615
								if( diMinus > 41.5189 )
									ret := -1.000000 // sell
							if( smoothedDirectionalMovementMinus > 0.004528 )
								if( trueRange <= 0.00281 )
									ret := -0.833333 // sell
								if( trueRange > 0.00281 )
									ret := -1.000000 // sell
						if( trueRange > 0.009958 )
							if( smoothedDirectionalMovementPlus <= 0.007216 )
								if( dx <= 18.2835 )
									ret := -0.909091 // sell
								if( dx > 18.2835 )
									ret := -0.222222
							if( smoothedDirectionalMovementPlus > 0.007216 )
								ret := -0.052632
					if( diPlus > 49.9855 )
						if( smoothedDirectionalMovementPlus <= 0.020288 )
							if( trueRange <= 0.007974 )
								if( smoothedDirectionalMovementPlus <= 0.007037 )
									ret := -0.211429
								if( smoothedDirectionalMovementPlus > 0.007037 )
									ret := -0.559524
							if( trueRange > 0.007974 )
								if( smoothedDirectionalMovementMinus <= 0.004329 )
									ret := -0.013566
								if( smoothedDirectionalMovementMinus > 0.004329 )
									ret := -0.299435
						if( smoothedDirectionalMovementPlus > 0.020288 )
							if( diPlus <= 64.327 )
								ret := 0.823529 // buy
							if( diPlus > 64.327 )
								ret := 0.333333
			if( trueRange > 0.011511 )
				if( smoothedTrueRange <= 0.07076 )
					if( diMinus <= 24.0385 )
						if( directionalMovementPlus <= 0.062815 )
							if( dx <= 83.652 )
								if( smoothedTrueRange <= 0.041329 )
									ret := -0.350575
								if( smoothedTrueRange > 0.041329 )
									ret := -0.600000
							if( dx > 83.652 )
								if( adx <= 77.4851 )
									ret := 0.013889
								if( adx > 77.4851 )
									ret := -0.750000 // sell
						if( directionalMovementPlus > 0.062815 )
							if( diMinus <= 11.9293 )
								if( smoothedDirectionalMovementMinus <= 0.004419 )
									ret := -0.651515
								if( smoothedDirectionalMovementMinus > 0.004419 )
									ret := 0.750000 // buy
							if( diMinus > 11.9293 )
								if( smoothedDirectionalMovementPlus <= 0.017712 )
									ret := -0.717949 // sell
								if( smoothedDirectionalMovementPlus > 0.017712 )
									ret := -1.000000 // sell
					if( diMinus > 24.0385 )
						if( diPlus <= 74.2522 )
							if( directionalMovementPlus <= 0.000184 )
								if( directionalMovementMinus <= 0.011774 )
									ret := -0.397727
								if( directionalMovementMinus > 0.011774 )
									ret := 0.283887
							if( directionalMovementPlus > 0.000184 )
								if( diPlus <= 64.5265 )
									ret := -0.260549
								if( diPlus > 64.5265 )
									ret := -0.602804
						if( diPlus > 74.2522 )
							ret := 1.000000 // buy
				if( smoothedTrueRange > 0.07076 )
					if( diMinus <= 7.11653 )
						if( diPlus <= 64.5356 )
							if( dx <= 78.6881 )
								ret := 0.333333
							if( dx > 78.6881 )
								if( dx <= 86.4263 )
									ret := -0.842105 // sell
								if( dx > 86.4263 )
									ret := -0.363636
						if( diPlus > 64.5356 )
							if( trueRange <= 0.388253 )
								if( directionalMovementPlus <= 0.003553 )
									ret := 0.675676
								if( directionalMovementPlus > 0.003553 )
									ret := -0.636364
							if( trueRange > 0.388253 )
								ret := -1.000000 // sell
					if( diMinus > 7.11653 )
						if( diMinus <= 17.0159 )
							if( diMinus <= 12.3594 )
								if( directionalMovementPlus <= 0.144573 )
									ret := 0.974359 // buy
								if( directionalMovementPlus > 0.144573 )
									ret := 0.636364
							if( diMinus > 12.3594 )
								ret := 0.666667
						if( diMinus > 17.0159 )
							ret := -0.166667
	if( diMinus > 43.9974 )
		if( directionalMovementPlus <= 0.01066 )
			if( directionalMovementMinus <= 0.011539 )
				if( smoothedTrueRange <= 0.022449 )
					if( diMinus <= 78.35 )
						if( diPlus <= 29.2414 )
							if( smoothedDirectionalMovementPlus <= 0.000952 )
								if( smoothedDirectionalMovementPlus <= 4e-06 )
									ret := 0.392857
								if( smoothedDirectionalMovementPlus > 4e-06 )
									ret := 0.022124
							if( smoothedDirectionalMovementPlus > 0.000952 )
								if( dx <= 51.3727 )
									ret := 0.228315
								if( dx > 51.3727 )
									ret := 0.382629
						if( diPlus > 29.2414 )
							if( adx <= 28.8475 )
								if( directionalMovementMinus <= 2e-05 )
									ret := 0.045614
								if( directionalMovementMinus > 2e-05 )
									ret := 0.266667
							if( adx > 28.8475 )
								if( dx <= 16.5301 )
									ret := 0.112971
								if( dx > 16.5301 )
									ret := -0.284519
					if( diMinus > 78.35 )
						if( diMinus <= 90.9843 )
							if( dx <= 61.9391 )
								if( smoothedDirectionalMovementPlus <= 0.000769 )
									ret := 0.700000 // buy
								if( smoothedDirectionalMovementPlus > 0.000769 )
									ret := 1.000000 // buy
							if( dx > 61.9391 )
								if( smoothedTrueRange <= 0.004668 )
									ret := 0.076923
								if( smoothedTrueRange > 0.004668 )
									ret := 0.585366
						if( diMinus > 90.9843 )
							ret := -0.181818
				if( smoothedTrueRange > 0.022449 )
					if( smoothedDirectionalMovementPlus <= 0.002776 )
						if( diPlus <= 1.24372 )
							if( diMinus <= 47.518 )
								if( smoothedDirectionalMovementMinus <= 0.015616 )
									ret := 0.150000
								if( smoothedDirectionalMovementMinus > 0.015616 )
									ret := -0.535714
							if( diMinus > 47.518 )
								if( smoothedDirectionalMovementMinus <= 0.023292 )
									ret := 0.108108
								if( smoothedDirectionalMovementMinus > 0.023292 )
									ret := 0.750000 // buy
						if( diPlus > 1.24372 )
							if( adx <= 73.9443 )
								if( smoothedTrueRange <= 0.027425 )
									ret := -0.155738
								if( smoothedTrueRange > 0.027425 )
									ret := -0.626866
							if( adx > 73.9443 )
								if( dx <= 92.3028 )
									ret := 0.590909
								if( dx > 92.3028 )
									ret := -0.937500 // sell
					if( smoothedDirectionalMovementPlus > 0.002776 )
						if( diMinus <= 50.9909 )
							if( diMinus <= 47.9808 )
								if( adx <= 80.3094 )
									ret := 0.019324
								if( adx > 80.3094 )
									ret := 1.000000 // buy
							if( diMinus > 47.9808 )
								if( smoothedTrueRange <= 0.044629 )
									ret := -0.487654
								if( smoothedTrueRange > 0.044629 )
									ret := 0.444444
						if( diMinus > 50.9909 )
							if( diPlus <= 7.13344 )
								if( diPlus <= 4.88506 )
									ret := 1.000000 // buy
								if( diPlus > 4.88506 )
									ret := 0.818182 // buy
							if( diPlus > 7.13344 )
								if( diMinus <= 55.4087 )
									ret := 0.446237
								if( diMinus > 55.4087 )
									ret := 0.127737
			if( directionalMovementMinus > 0.011539 )
				if( dx <= 24.9662 )
					if( directionalMovementMinus <= 0.020769 )
						if( trueRange <= 0.019438 )
							if( directionalMovementMinus <= 0.015006 )
								if( smoothedTrueRange <= 0.016716 )
									ret := 0.611940
								if( smoothedTrueRange > 0.016716 )
									ret := 0.023256
							if( directionalMovementMinus > 0.015006 )
								if( smoothedDirectionalMovementMinus <= 0.004186 )
									ret := 0.307692
								if( smoothedDirectionalMovementMinus > 0.004186 )
									ret := 0.754237 // buy
						if( trueRange > 0.019438 )
							if( diPlus <= 35.2231 )
								if( diPlus <= 31.9091 )
									ret := -0.272727
								if( diPlus > 31.9091 )
									ret := -0.625000
							if( diPlus > 35.2231 )
								if( directionalMovementMinus <= 0.019034 )
									ret := -0.105263
								if( directionalMovementMinus > 0.019034 )
									ret := 0.321285
					if( directionalMovementMinus > 0.020769 )
						if( smoothedDirectionalMovementPlus <= 0.008575 )
							if( adx <= 29.7466 )
								if( dx <= 14.2951 )
									ret := 0.701863 // buy
								if( dx > 14.2951 )
									ret := 0.878261 // buy
							if( adx > 29.7466 )
								if( smoothedTrueRange <= 0.012714 )
									ret := 0.000000
								if( smoothedTrueRange > 0.012714 )
									ret := 0.734694 // buy
						if( smoothedDirectionalMovementPlus > 0.008575 )
							if( smoothedTrueRange <= 0.021376 )
								if( smoothedDirectionalMovementPlus <= 0.009357 )
									ret := -0.272727
								if( smoothedDirectionalMovementPlus > 0.009357 )
									ret := 0.210526
							if( smoothedTrueRange > 0.021376 )
								if( directionalMovementMinus <= 0.070277 )
									ret := 0.633333
								if( directionalMovementMinus > 0.070277 )
									ret := 0.287879
				if( dx > 24.9662 )
					if( directionalMovementMinus <= 0.0186 )
						if( diPlus <= 2.61847 )
							if( trueRange <= 0.035951 )
								if( trueRange <= 0.022063 )
									ret := -0.437500
								if( trueRange > 0.022063 )
									ret := 0.473684
							if( trueRange > 0.035951 )
								ret := -0.785714 // sell
						if( diPlus > 2.61847 )
							if( dx <= 36.9167 )
								if( smoothedDirectionalMovementMinus <= 0.007662 )
									ret := 0.565217
								if( smoothedDirectionalMovementMinus > 0.007662 )
									ret := -0.076923
							if( dx > 36.9167 )
								if( smoothedTrueRange <= 0.037459 )
									ret := 0.735537 // buy
								if( smoothedTrueRange > 0.037459 )
									ret := 0.372549
					if( directionalMovementMinus > 0.0186 )
						if( directionalMovementMinus <= 0.025043 )
							if( dx <= 94.587 )
								if( smoothedDirectionalMovementMinus <= 0.01347 )
									ret := 0.014620
								if( smoothedDirectionalMovementMinus > 0.01347 )
									ret := 0.366906
							if( dx > 94.587 )
								if( trueRange <= 0.035544 )
									ret := -0.125000
								if( trueRange > 0.035544 )
									ret := -1.000000 // sell
						if( directionalMovementMinus > 0.025043 )
							if( smoothedDirectionalMovementMinus <= 0.010736 )
								if( smoothedDirectionalMovementPlus <= 0.004289 )
									ret := 0.640127
								if( smoothedDirectionalMovementPlus > 0.004289 )
									ret := 0.258621
							if( smoothedDirectionalMovementMinus > 0.010736 )
								if( adx <= 54.1662 )
									ret := 0.148666
								if( adx > 54.1662 )
									ret := 0.482143
		if( directionalMovementPlus > 0.01066 )
			if( diPlus <= 23.0481 )
				if( trueRange <= 0.033849 )
					if( smoothedTrueRange <= 0.030036 )
						if( diMinus <= 54.1875 )
							if( diMinus <= 48.5766 )
								if( smoothedDirectionalMovementMinus <= 0.010265 )
									ret := -0.600000
								if( smoothedDirectionalMovementMinus > 0.010265 )
									ret := 0.666667
							if( diMinus > 48.5766 )
								ret := -1.000000 // sell
						if( diMinus > 54.1875 )
							if( trueRange <= 0.021737 )
								ret := 0.550000
							if( trueRange > 0.021737 )
								ret := 0.272727
					if( smoothedTrueRange > 0.030036 )
						if( smoothedDirectionalMovementMinus <= 0.017452 )
							ret := -0.785714 // sell
						if( smoothedDirectionalMovementMinus > 0.017452 )
							ret := -0.307692
				if( trueRange > 0.033849 )
					if( diPlus <= 17.43 )
						if( dx <= 60.1407 )
							if( smoothedTrueRange <= 0.024559 )
								ret := 0.636364
							if( smoothedTrueRange > 0.024559 )
								if( smoothedDirectionalMovementPlus <= 0.019506 )
									ret := -0.333333
								if( smoothedDirectionalMovementPlus > 0.019506 )
									ret := -1.000000 // sell
						if( dx > 60.1407 )
							if( adx <= 56.5654 )
								if( smoothedDirectionalMovementPlus <= 0.003882 )
									ret := -0.681818
								if( smoothedDirectionalMovementPlus > 0.003882 )
									ret := 0.666667
							if( adx > 56.5654 )
								if( smoothedTrueRange <= 0.080111 )
									ret := 0.892857 // buy
								if( smoothedTrueRange > 0.080111 )
									ret := 1.000000 // buy
					if( diPlus > 17.43 )
						if( smoothedDirectionalMovementMinus <= 0.027799 )
							if( diMinus <= 48.4221 )
								ret := 0.681818
							if( diMinus > 48.4221 )
								if( smoothedDirectionalMovementMinus <= 0.025705 )
									ret := 1.000000 // buy
								if( smoothedDirectionalMovementMinus > 0.025705 )
									ret := 0.923077 // buy
						if( smoothedDirectionalMovementMinus > 0.027799 )
							ret := 0.200000
			if( diPlus > 23.0481 )
				if( smoothedDirectionalMovementMinus <= 0.012116 )
					if( directionalMovementMinus <= 0.012201 )
						if( dx <= 11.2654 )
							if( diPlus <= 50.0063 )
								if( smoothedDirectionalMovementPlus <= 0.009764 )
									ret := -0.565574
								if( smoothedDirectionalMovementPlus > 0.009764 )
									ret := 0.163265
							if( diPlus > 50.0063 )
								if( trueRange <= 0.030971 )
									ret := 0.153846
								if( trueRange > 0.030971 )
									ret := -0.675676
						if( dx > 11.2654 )
							if( smoothedDirectionalMovementPlus <= 0.007708 )
								if( trueRange <= 0.013401 )
									ret := 0.700000 // buy
								if( trueRange > 0.013401 )
									ret := -0.254386
							if( smoothedDirectionalMovementPlus > 0.007708 )
								if( diPlus <= 39.6236 )
									ret := 0.000000
								if( diPlus > 39.6236 )
									ret := 0.777778 // buy
					if( directionalMovementMinus > 0.012201 )
						if( adx <= 21.8225 )
							ret := 0.714286 // buy
						if( adx > 21.8225 )
							ret := 0.333333
				if( smoothedDirectionalMovementMinus > 0.012116 )
					if( diMinus <= 46.8019 )
						if( smoothedTrueRange <= 0.033739 )
							if( directionalMovementPlus <= 0.029206 )
								ret := -0.333333
							if( directionalMovementPlus > 0.029206 )
								ret := -0.724138 // sell
						if( smoothedTrueRange > 0.033739 )
							if( smoothedTrueRange <= 0.041707 )
								ret := 0.666667
							if( smoothedTrueRange > 0.041707 )
								ret := 0.153846
					if( diMinus > 46.8019 )
						if( smoothedTrueRange <= 0.0258 )
							if( diPlus <= 37.3556 )
								if( smoothedDirectionalMovementMinus <= 0.013546 )
									ret := -0.878788 // sell
								if( smoothedDirectionalMovementMinus > 0.013546 )
									ret := -0.187500
							if( diPlus > 37.3556 )
								if( dx <= 10.9719 )
									ret := -0.450000
								if( dx > 10.9719 )
									ret := 0.300000
						if( smoothedTrueRange > 0.0258 )
							if( smoothedTrueRange <= 0.044004 )
								if( trueRange <= 0.031031 )
									ret := -0.661538
								if( trueRange > 0.031031 )
									ret := -0.858696 // sell
							if( smoothedTrueRange > 0.044004 )
								ret := -0.461538
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator ADX_and_DI 
//@version=5
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © BeikabuOyaji

//indicator "ADX and DI for v5", overlay=false)

// Input parameters
len = input(14, title="Length")
th = input(20, title="Threshold")

// Calculate True Range
trueRange = math.max(math.max(high - low, math.abs(high - nz(close[1]))), math.abs(low - nz(close[1])))

// Calculate Directional Movements
directionalMovementPlus = high - nz(high[1]) > nz(low[1]) - low ? math.max(high - nz(high[1]), 0) : 0
directionalMovementMinus = nz(low[1]) - low > high - nz(high[1]) ? math.max(nz(low[1]) - low, 0) : 0

// Initialize and calculate smoothed values
var float smoothedTrueRange = 0
var float smoothedDirectionalMovementPlus = 0
var float smoothedDirectionalMovementMinus = 0

smoothedTrueRange := nz(smoothedTrueRange[1]) - (nz(smoothedTrueRange[1]) / len) + trueRange
smoothedDirectionalMovementPlus := nz(smoothedDirectionalMovementPlus[1]) - (nz(smoothedDirectionalMovementPlus[1]) / len) + directionalMovementPlus
smoothedDirectionalMovementMinus := nz(smoothedDirectionalMovementMinus[1]) - (nz(smoothedDirectionalMovementMinus[1]) / len) + directionalMovementMinus

// Calculate DI+ and DI-
diPlus = (smoothedDirectionalMovementPlus / smoothedTrueRange) * 100
diMinus = (smoothedDirectionalMovementMinus / smoothedTrueRange) * 100

// Calculate DX and ADX
dx = math.abs(diPlus - diMinus) / (diPlus + diMinus) * 100
adx = ta.sma(dx, len)

// Plot DI+, DI-, and ADX
plot(diPlus, color=color.green, title="DI+")
plot(diMinus, color=color.red, title="DI-")
plot(adx, color=color.navy, title="ADX")

// Plot threshold line
hline(th, "Threshold", color=color.black)

// EXPLANATION OF THE STRATEGY
//The provided Pine Script implements a trading strategy that includes stop loss (SL) and multiple take profit (TP) levels,
//with an option to activate a trailing stop at the third TP level. Here's a detailed breakdown of its components and functionality:

//Variables Initialization:
var float stop = na
var float limit1 = na
var float limit2 = na

// Converts a percentage to points based on the average position price and the minimum tick size.
percent2points(percent) =>
    strategy.position_avg_price * percent / 100 / syminfo.mintick

// Stop Loss and Take Profit Inputs:
//Defines inputs for stop loss and three take profit levels in percentage terms.
sl = percent2points(input(2.92, title="stop loss %%"))
tp1 = percent2points(input(1.12, title="take profit 1 %%"))
tp2 = percent2points(input(2.31, title="take profit 2 %%"))
tp3 = percent2points(input(3.91, title="take profit 3 %%"))
activateTrailingOnThirdStep = input(false,title="activate trailing on third stage (tp3 is amount, tp2 is offset level)")
log.info("Stop Loss (sl):", sl," Take Profit 1 (tp1):", tp1, " Take Profit 2 (tp2):", tp2," Take Profit 3 (tp3):", tp3)

// Current Profit Calculation:
//Calculates the current profit in points based on the position size and price.
curProfitInPts() =>
    if strategy.position_size > 0
        (high - strategy.position_avg_price) / syminfo.mintick
    else if strategy.position_size < 0
        (strategy.position_avg_price - low) / syminfo.mintick
    else
        0
// Stop Loss and Profit Target Price Calculations:
//Determines the stop loss and profit target prices based on the position size and offset points.
calcStopLossPrice(OffsetPts) =>
    if strategy.position_size > 0
        strategy.position_avg_price - OffsetPts * syminfo.mintick
    else if strategy.position_size < 0
        strategy.position_avg_price + OffsetPts * syminfo.mintick
    else
        0
calcProfitTrgtPrice(OffsetPts) =>
    calcStopLossPrice(-OffsetPts)
// Current Stage Determination:
//Determines the current stage of the trade based on the profit points reached.
getCurrentStage() =>
    var stage = 0
    if strategy.position_size == 0
        stage := 0
    if stage == 0 and strategy.position_size != 0
        stage := 1
    else if stage == 1 and curProfitInPts() >= tp1
        stage := 2
    else if stage == 2 and curProfitInPts() >= tp2
        stage := 3
    stage
stopLevel = -1.
profitLevel = calcProfitTrgtPrice(tp3)

log.info("Stop Level:", stopLevel)
log.info("Profit Level:", profitLevel)
//This part of the strategy sets up exit conditions based on the current stage of the trade and uses the same exit ID "x" to modify the exit parameters dynamically.
//The exit parameters include stop loss, take profit, and comments for each stage.
// based on current stage set up exit
// note: we use same exit ids ("x") consciously, for MODIFY the exit's parameters
curStage = getCurrentStage()
float op_operation = decision_tree_0_SNAP_1Min_b316283f(dx, diMinus, directionalMovementMinus, adx, diPlus, directionalMovementPlus, smoothedTrueRange, smoothedDirectionalMovementPlus, smoothedDirectionalMovementMinus, trueRange)

log.info("Decision Tree Operation (op_operation):", op_operation)
if (op_operation <= 0)
    if curStage == 1
        stopLevel := calcStopLossPrice(sl)
        strategy.exit("x", loss = sl, profit = tp3, comment = "sl or tp3")
    else if curStage == 2
        stopLevel := calcStopLossPrice(0)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "breakeven or tp3")
    else if curStage == 3
        stopLevel := calcStopLossPrice(-tp1)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "tp1 or tp3")
    else
        strategy.cancel("x")


//SIGNAL MANAGE    User Adjustments and Risk Management
// The user can adjust the threshold values for op_operation to control the level of risk they are willing to take:
// Lower op_operation Threshold for Buy Signal (e.g., 0.5 instead of 0.55):
//     Effect: Generates more buy signals, increasing the frequency of trades. This is suitable for a user willing to take more risks and potentially capture more trading opportunities.
// Higher op_operation Threshold for Buy Signal (e.g., 0.8 instead of 0.55):
//     Effect: Generates fewer buy signals, reducing the frequency of trades. This is suitable for a user seeking to take fewer risks and only enter trades under more favorable conditions.
// Lower op_operation Threshold for Signal Closure (e.g., -0.8 instead of -0.9):
//     Effect: Closes positions less frequently, allowing trades more room to recover from temporary unfavorable conditions. This increases risk but can capture larger gains if the market reverses favorably.
// Higher op_operation Threshold for Signal Closure (e.g., -0.95 instead of -0.9):
//     Effect: Closes positions more frequently, exiting trades quickly at the first sign of unfavorable conditions. This decreases risk but may result in missed opportunities for recovery.
//Signal BUY
FIXED_DOLLAR_AMOUNT  = 10000
positionSize = FIXED_DOLLAR_AMOUNT / close
log.info("Position Size (in dollars $",FIXED_DOLLAR_AMOUNT,"):", positionSize)

if (op_operation >= 0.55)
    stop := close * 0.965
    limit1 := close * 1.03
    limit2 := close * 1.02
    strategy.entry("x", strategy.long, qty=positionSize, stop=stop, comment="in")
//Signal SELL
if (op_operation <= -0.9)
    strategy.close("x", comment = "under Le1")

// Impact on the Dataset
//Stop Loss (SL): Limits the maximum loss by exiting the position if the price moves against the trade by a specified percentage.
//Take Profit (TP1, TP2, TP3): Defines profit-taking levels to secure gains at different stages.
//Trailing Stop: Optionally activates a trailing stop at the third TP level to lock in profits while allowing for further gains if the price continues to move favorably.
//Position Entry and Exit: The strategy's buy and sell signals determine when to enter and exit positions, influencing the dataset by marking the points of trade execution and closure.
//Current Stage Tracking: Monitors the trade's progress through predefined stages, adjusting stop and profit levels accordingly.
//This strategy is designed to manage risk and maximize profits through a structured approach, incorporating multiple exit levels and dynamic adjustments based on market conditions. The dataset will reflect these actions, showing entries, exits, stop loss activations, and profit-taking events, providing valuable information for backtesting and performance analysis.
//Random forest AI offers significant advantages in trading, including the ability to handle large data sets, reduce overfitting and provide more robust predictions through the aggregation of multiple decision trees.

// NOTE: While the Tuisku team stands behind the quality and effectiveness of this trading strategy,
// PLEASE be aware that there is NO GUARANTEE of specific results or profits. TRADING INVOLVES SIGNIFICANT RISK, and it is important to use this strategy with careful consideration of your financial situation and risk tolerance.
// For further information and support, please contact us at Tuisku.eu.


