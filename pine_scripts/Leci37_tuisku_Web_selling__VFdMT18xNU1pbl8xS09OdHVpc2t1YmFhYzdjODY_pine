//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Blai5_Koncorde_v10
// ID_model: TWLO_15Min_1KON_baac7c86 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_TWLO_15Min_1KON_baac7c86", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_TWLO_15Min_baac7c86(nvi, nvi_ema, marron_mean, source, azul, verde_azul, verde_mean, xmf, pvimin, stoc, media, tprice, marron, pvim, pvimax, xrsi, oscp, pvi, nvimax, nvimin, verde, verde_media, azul_mean, nvim, BollOsc, pvi_ema, media_azul)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( BollOsc <= -16.9451 )
		if( pvimin <= 1.25791 )
			if( tprice <= 117.288 )
				if( azul_mean <= -104.195 )
					if( marron_mean <= 11.5828 )
						if( media_azul <= 103.433 )
							ret := -0.500000
						if( media_azul > 103.433 )
							if( nvimin <= 0.570459 )
								ret := 1.000000 // buy
							if( nvimin > 0.570459 )
								ret := 0.500000
					if( marron_mean > 11.5828 )
						if( oscp <= 8.17131 )
							if( media <= 46.8339 )
								if( media_azul <= 105.763 )
									ret := -1.000000 // sell
								if( media_azul > 105.763 )
									ret := 0.200000
							if( media > 46.8339 )
								ret := -1.000000 // sell
						if( oscp > 8.17131 )
							ret := 0.250000
				if( azul_mean > -104.195 )
					if( verde_media <= -157.66 )
						if( stoc <= 24.8684 )
							if( source <= 82.6787 )
								if( azul_mean <= -10.4071 )
									ret := 0.285714
								if( azul_mean > -10.4071 )
									ret := 1.000000 // buy
							if( source > 82.6787 )
								if( verde_media <= -192.894 )
									ret := 0.500000
								if( verde_media > -192.894 )
									ret := -0.846154 // sell
						if( stoc > 24.8684 )
							if( marron <= 11.2285 )
								if( pvimax <= 1.15922 )
									ret := -0.904762 // sell
								if( pvimax > 1.15922 )
									ret := -0.333333
							if( marron > 11.2285 )
								if( pvim <= 0.547663 )
									ret := 0.250000
								if( pvim > 0.547663 )
									ret := 0.500000
					if( verde_media > -157.66 )
						if( marron_mean <= 57.7426 )
							if( BollOsc <= -29.5293 )
								if( nvimin <= 0.992682 )
									ret := 0.142140
								if( nvimin > 0.992682 )
									ret := -0.248780
							if( BollOsc > -29.5293 )
								if( pvim <= 0.934132 )
									ret := 0.117601
								if( pvim > 0.934132 )
									ret := 0.007778
						if( marron_mean > 57.7426 )
							if( xmf <= 45.9494 )
								if( nvimin <= 0.474493 )
									ret := -0.063559
								if( nvimin > 0.474493 )
									ret := 0.305825
							if( xmf > 45.9494 )
								if( nvimin <= 0.899037 )
									ret := 0.393539
								if( nvimin > 0.899037 )
									ret := -0.177778
			if( tprice > 117.288 )
				if( nvimin <= 1.11472 )
					if( verde_azul <= 30.8966 )
						if( verde_mean <= -30.0994 )
							if( marron <= 4.00907 )
								if( source <= 183.812 )
									ret := 0.622222
								if( source > 183.812 )
									ret := -0.100000
							if( marron > 4.00907 )
								if( xmf <= 69.5248 )
									ret := -0.593220
								if( xmf > 69.5248 )
									ret := 1.000000 // buy
						if( verde_mean > -30.0994 )
							if( oscp <= -18.1756 )
								if( azul <= -11.8119 )
									ret := -0.051546
								if( azul > -11.8119 )
									ret := 0.341317
							if( oscp > -18.1756 )
								if( nvim <= 0.911545 )
									ret := 0.369231
								if( nvim > 0.911545 )
									ret := 0.649231
					if( verde_azul > 30.8966 )
						if( xrsi <= 37.1665 )
							if( nvi_ema <= 0.472871 )
								if( stoc <= 35.257 )
									ret := 0.684211
								if( stoc > 35.257 )
									ret := -0.500000
							if( nvi_ema > 0.472871 )
								if( pvimax <= 1.23793 )
									ret := -0.040816
								if( pvimax > 1.23793 )
									ret := -0.575758
						if( xrsi > 37.1665 )
							if( tprice <= 149.026 )
								if( tprice <= 133.198 )
									ret := 0.252525
								if( tprice > 133.198 )
									ret := -0.515152
							if( tprice > 149.026 )
								if( tprice <= 198.026 )
									ret := 0.727273 // buy
								if( tprice > 198.026 )
									ret := 0.055556
				if( nvimin > 1.11472 )
					if( verde_media <= -33.2317 )
						if( media_azul <= 66.9436 )
							if( verde_mean <= -46.1597 )
								if( azul_mean <= -25.339 )
									ret := 0.000000
								if( azul_mean > -25.339 )
									ret := -0.733333 // sell
							if( verde_mean > -46.1597 )
								if( nvi <= 1.14269 )
									ret := 0.584906
								if( nvi > 1.14269 )
									ret := 0.043624
						if( media_azul > 66.9436 )
							if( verde <= 25.7369 )
								if( marron <= 21.3788 )
									ret := -0.291139
								if( marron > 21.3788 )
									ret := -0.875000 // sell
							if( verde > 25.7369 )
								if( nvi_ema <= 1.26783 )
									ret := 1.000000 // buy
								if( nvi_ema > 1.26783 )
									ret := 0.000000
					if( verde_media > -33.2317 )
						if( xmf <= 32.298 )
							if( oscp <= -2.06265 )
								if( verde_azul <= -10.6094 )
									ret := 0.730769 // buy
								if( verde_azul > -10.6094 )
									ret := 0.406542
							if( oscp > -2.06265 )
								if( media <= 22.7977 )
									ret := -0.466667
								if( media > 22.7977 )
									ret := 0.240741
						if( xmf > 32.298 )
							if( verde <= 7.9208 )
								if( xmf <= 37.4683 )
									ret := 0.095238
								if( xmf > 37.4683 )
									ret := -0.638889
							if( verde > 7.9208 )
								if( media <= 57.4067 )
									ret := 0.089636
								if( media > 57.4067 )
									ret := 0.636364
		if( pvimin > 1.25791 )
			if( stoc <= 6.76412 )
				if( verde_mean <= -15.1235 )
					if( verde <= -42.024 )
						if( pvimin <= 1.35136 )
							if( azul_mean <= 1.42107 )
								if( verde_mean <= -26.2043 )
									ret := 0.750000 // buy
								if( verde_mean > -26.2043 )
									ret := 0.000000
							if( azul_mean > 1.42107 )
								ret := -0.250000
						if( pvimin > 1.35136 )
							if( azul <= -21.3428 )
								if( nvi <= 1.29548 )
									ret := -0.444444
								if( nvi > 1.29548 )
									ret := -1.000000 // sell
							if( azul > -21.3428 )
								if( azul_mean <= -17.9626 )
									ret := 0.833333 // buy
								if( azul_mean > -17.9626 )
									ret := -0.040000
					if( verde > -42.024 )
						if( azul <= 2.77125 )
							if( pvi <= 1.25919 )
								if( verde_media <= -37.4592 )
									ret := -0.333333
								if( verde_media > -37.4592 )
									ret := 0.500000
							if( pvi > 1.25919 )
								if( nvimax <= 0.579395 )
									ret := 0.425000
								if( nvimax > 0.579395 )
									ret := 0.750000 // buy
						if( azul > 2.77125 )
							if( xmf <= 17.7984 )
								if( media <= 7.70333 )
									ret := 1.000000 // buy
								if( media > 7.70333 )
									ret := 0.500000
							if( xmf > 17.7984 )
								if( verde_azul <= -27.5339 )
									ret := 0.000000
								if( verde_azul > -27.5339 )
									ret := -0.714286 // sell
				if( verde_mean > -15.1235 )
					if( pvimin <= 1.26025 )
						if( pvim <= 1.25992 )
							ret := -1.000000 // sell
						if( pvim > 1.25992 )
							ret := -0.250000
					if( pvimin > 1.26025 )
						if( oscp <= -3.2169 )
							if( BollOsc <= -55.2202 )
								if( marron_mean <= 6.00548 )
									ret := -0.785714 // sell
								if( marron_mean > 6.00548 )
									ret := 0.065217
							if( BollOsc > -55.2202 )
								if( BollOsc <= -40.4895 )
									ret := 0.500000
								if( BollOsc > -40.4895 )
									ret := 0.096045
						if( oscp > -3.2169 )
							if( xrsi <= 35.9079 )
								if( xrsi <= 29.6448 )
									ret := -0.434783
								if( xrsi > 29.6448 )
									ret := 0.555556
							if( xrsi > 35.9079 )
								if( verde <= 13.9653 )
									ret := 0.000000
								if( verde > 13.9653 )
									ret := -0.857143 // sell
			if( stoc > 6.76412 )
				if( marron_mean <= 54.0052 )
					if( pvimax <= 1.68139 )
						if( stoc <= 37.3141 )
							if( nvi_ema <= 1.57979 )
								if( nvi_ema <= 1.48883 )
									ret := 0.025622
								if( nvi_ema > 1.48883 )
									ret := 0.255670
							if( nvi_ema > 1.57979 )
								if( xmf <= 21.1425 )
									ret := 0.066667
								if( xmf > 21.1425 )
									ret := -0.469565
						if( stoc > 37.3141 )
							if( oscp <= -47.7379 )
								if( nvi_ema <= 1.46692 )
									ret := 0.606061
								if( nvi_ema > 1.46692 )
									ret := -0.250000
							if( oscp > -47.7379 )
								if( pvim <= 1.52521 )
									ret := -0.264451
								if( pvim > 1.52521 )
									ret := 0.091954
					if( pvimax > 1.68139 )
						if( media <= 9.12397 )
							if( azul_mean <= 35.1405 )
								if( pvimax <= 1.69481 )
									ret := 0.173913
								if( pvimax > 1.69481 )
									ret := 0.796296 // buy
							if( azul_mean > 35.1405 )
								if( oscp <= -28.809 )
									ret := -0.875000 // sell
								if( oscp > -28.809 )
									ret := 0.250000
						if( media > 9.12397 )
							if( pvi_ema <= 1.65978 )
								if( verde_media <= -45.2113 )
									ret := 0.054054
								if( verde_media > -45.2113 )
									ret := -0.683230
							if( pvi_ema > 1.65978 )
								if( xmf <= 19.4786 )
									ret := -0.436842
								if( xmf > 19.4786 )
									ret := 0.018711
				if( marron_mean > 54.0052 )
					if( xmf <= 62.2536 )
						if( azul_mean <= -48.7098 )
							if( source <= 138.106 )
								ret := -0.250000
							if( source > 138.106 )
								ret := -1.000000 // sell
						if( azul_mean > -48.7098 )
							if( marron <= 37.3942 )
								if( media <= 40.1742 )
									ret := -0.909091 // sell
								if( media > 40.1742 )
									ret := 0.206897
							if( marron > 37.3942 )
								if( verde_azul <= 70.5362 )
									ret := -0.183673
								if( verde_azul > 70.5362 )
									ret := 0.416667
					if( xmf > 62.2536 )
						if( azul <= -71.3938 )
							if( xrsi <= 35.3188 )
								ret := 0.000000
							if( xrsi > 35.3188 )
								ret := -1.000000 // sell
						if( azul > -71.3938 )
							if( media_azul <= 57.8162 )
								if( verde_mean <= 37.8399 )
									ret := 0.666667
								if( verde_mean > 37.8399 )
									ret := -0.342105
							if( media_azul > 57.8162 )
								if( verde <= 63.9798 )
									ret := 0.508000
								if( verde > 63.9798 )
									ret := -0.172414
	if( BollOsc > -16.9451 )
		if( media <= 58.884 )
			if( pvimin <= -0.008024 )
				if( media_azul <= -0.717566 )
					if( azul_mean <= 4.17313 )
						if( azul_mean <= -26.8448 )
							ret := 1.000000 // buy
						if( azul_mean > -26.8448 )
							ret := 0.166667
					if( azul_mean > 4.17313 )
						if( nvi <= -0.079216 )
							if( pvimin <= -0.123833 )
								ret := 0.600000
							if( pvimin > -0.123833 )
								ret := -0.500000
						if( nvi > -0.079216 )
							if( verde_azul <= -3.78528 )
								if( xmf <= 41.2004 )
									ret := -0.931818 // sell
								if( xmf > 41.2004 )
									ret := -0.444444
							if( verde_azul > -3.78528 )
								if( oscp <= -3.03523 )
									ret := -0.066667
								if( oscp > -3.03523 )
									ret := -0.800000 // sell
				if( media_azul > -0.717566 )
					if( pvimax <= 0.072504 )
						if( verde_media <= 50.5527 )
							if( marron_mean <= 62.4022 )
								if( nvi_ema <= -0.096039 )
									ret := -0.063158
								if( nvi_ema > -0.096039 )
									ret := 0.343365
							if( marron_mean > 62.4022 )
								if( verde <= 58.0131 )
									ret := -0.692308
								if( verde > 58.0131 )
									ret := -0.044248
						if( verde_media > 50.5527 )
							if( marron_mean <= 54.948 )
								if( verde_mean <= 57.4494 )
									ret := -0.846154 // sell
								if( verde_mean > 57.4494 )
									ret := -0.285714
							if( marron_mean > 54.948 )
								if( azul <= 23.5731 )
									ret := 0.105263
								if( azul > 23.5731 )
									ret := -0.800000 // sell
					if( pvimax > 0.072504 )
						if( media <= 31.017 )
							ret := 0.000000
						if( media > 31.017 )
							if( pvi_ema <= -0.003843 )
								ret := 1.000000 // buy
							if( pvi_ema > -0.003843 )
								ret := 0.500000
			if( pvimin > -0.008024 )
				if( verde_azul <= 118.553 )
					if( verde_media <= 44.8811 )
						if( azul <= 88.5959 )
							if( xrsi <= 37.6333 )
								if( verde_azul <= 25.5854 )
									ret := -0.433526
								if( verde_azul > 25.5854 )
									ret := -0.185294
							if( xrsi > 37.6333 )
								if( verde <= 16.3452 )
									ret := 0.228571
								if( verde > 16.3452 )
									ret := -0.050015
						if( azul > 88.5959 )
							if( BollOsc <= -1.05858 )
								if( pvimax <= 1.47507 )
									ret := -0.384615
								if( pvimax > 1.47507 )
									ret := 0.727273 // buy
							if( BollOsc > -1.05858 )
								if( xmf <= 5.9401 )
									ret := -0.250000
								if( xmf > 5.9401 )
									ret := -0.880597 // sell
					if( verde_media > 44.8811 )
						if( nvimax <= 1.47375 )
							if( BollOsc <= 45.8657 )
								if( verde_azul <= 108.124 )
									ret := -0.210419
								if( verde_azul > 108.124 )
									ret := 0.035857
							if( BollOsc > 45.8657 )
								if( xrsi <= 74.6037 )
									ret := -0.446809
								if( xrsi > 74.6037 )
									ret := 0.714286 // buy
						if( nvimax > 1.47375 )
							if( azul <= 21.0111 )
								if( nvimax <= 1.59125 )
									ret := 0.604651
								if( nvimax > 1.59125 )
									ret := -0.153846
							if( azul > 21.0111 )
								ret := -1.000000 // sell
				if( verde_azul > 118.553 )
					if( oscp <= 43.755 )
						if( stoc <= 29.3352 )
							if( xmf <= 62.0848 )
								ret := 0.000000
							if( xmf > 62.0848 )
								ret := -1.000000 // sell
						if( stoc > 29.3352 )
							if( xmf <= 85.4528 )
								if( BollOsc <= 43.7928 )
									ret := 0.337313
								if( BollOsc > 43.7928 )
									ret := -0.085106
							if( xmf > 85.4528 )
								if( azul <= 18.7161 )
									ret := 0.652174
								if( azul > 18.7161 )
									ret := -0.571429
					if( oscp > 43.755 )
						if( stoc <= 75.1966 )
							if( verde_mean <= 47.8706 )
								if( tprice <= 123.7 )
									ret := 0.486842
								if( tprice > 123.7 )
									ret := -0.500000
							if( verde_mean > 47.8706 )
								if( source <= 57.6256 )
									ret := -0.730337 // sell
								if( source > 57.6256 )
									ret := -0.089552
						if( stoc > 75.1966 )
							if( BollOsc <= 49.2461 )
								if( nvi_ema <= 1.30787 )
									ret := 0.829268 // buy
								if( nvi_ema > 1.30787 )
									ret := -0.500000
							if( BollOsc > 49.2461 )
								if( azul_mean <= 4.19473 )
									ret := -0.368421
								if( azul_mean > 4.19473 )
									ret := 0.500000
		if( media > 58.884 )
			if( BollOsc <= 36.8087 )
				if( pvi <= 0.959998 )
					if( nvimax <= 0.113872 )
						if( azul_mean <= 18.6196 )
							if( xmf <= 61.1814 )
								if( media_azul <= 107.066 )
									ret := 0.012581
								if( media_azul > 107.066 )
									ret := -0.264808
							if( xmf > 61.1814 )
								if( media <= 79.3676 )
									ret := -0.044413
								if( media > 79.3676 )
									ret := 0.190633
						if( azul_mean > 18.6196 )
							if( media_azul <= 69.0671 )
								if( xmf <= 35.6175 )
									ret := -0.166667
								if( xmf > 35.6175 )
									ret := 0.418231
							if( media_azul > 69.0671 )
								if( source <= 43.1303 )
									ret := -0.231707
								if( source > 43.1303 )
									ret := 0.346154
					if( nvimax > 0.113872 )
						if( nvimin <= 0.947049 )
							if( tprice <= 99.4826 )
								if( verde_azul <= 19.1919 )
									ret := -0.340909
								if( verde_azul > 19.1919 )
									ret := 0.302918
							if( tprice > 99.4826 )
								if( tprice <= 113.874 )
									ret := -0.086538
								if( tprice > 113.874 )
									ret := 0.781250 // buy
						if( nvimin > 0.947049 )
							if( pvi_ema <= 0.964778 )
								if( pvimax <= 0.752446 )
									ret := 0.459459
								if( pvimax > 0.752446 )
									ret := 0.817204 // buy
							if( pvi_ema > 0.964778 )
								ret := -0.200000
				if( pvi > 0.959998 )
					if( media_azul <= 62.4574 )
						if( pvi_ema <= 1.54053 )
							if( nvimax <= 0.565827 )
								if( tprice <= 62.37 )
									ret := 0.301980
								if( tprice > 62.37 )
									ret := -0.003384
							if( nvimax > 0.565827 )
								if( azul_mean <= 70.7807 )
									ret := -0.142435
								if( azul_mean > 70.7807 )
									ret := 0.769231 // buy
						if( pvi_ema > 1.54053 )
							if( pvimax <= 1.59122 )
								if( media_azul <= 48.3533 )
									ret := -0.190476
								if( media_azul > 48.3533 )
									ret := 0.637363
							if( pvimax > 1.59122 )
								if( nvimax <= 1.48235 )
									ret := 0.125541
								if( nvimax > 1.48235 )
									ret := -0.400000
					if( media_azul > 62.4574 )
						if( xrsi <= 59.351 )
							if( pvimax <= 1.61689 )
								if( nvimax <= 0.018686 )
									ret := -0.552632
								if( nvimax > 0.018686 )
									ret := 0.118026
							if( pvimax > 1.61689 )
								if( nvimin <= 1.40923 )
									ret := -0.277778
								if( nvimin > 1.40923 )
									ret := 0.070776
						if( xrsi > 59.351 )
							if( verde_mean <= 100.717 )
								if( media <= 81.3213 )
									ret := 0.087117
								if( media > 81.3213 )
									ret := -0.095897
							if( verde_mean > 100.717 )
								if( pvim <= 1.6863 )
									ret := 0.077564
								if( pvim > 1.6863 )
									ret := -0.361702
			if( BollOsc > 36.8087 )
				if( marron <= 95.3242 )
					if( source <= 25.5503 )
						if( media_azul <= 67.8681 )
							if( pvi <= -0.112894 )
								if( marron <= 81.0743 )
									ret := 0.500000
								if( marron > 81.0743 )
									ret := 0.941176 // buy
							if( pvi > -0.112894 )
								if( xmf <= 48.8474 )
									ret := 0.000000
								if( xmf > 48.8474 )
									ret := 0.500000
						if( media_azul > 67.8681 )
							if( marron_mean <= 87.6392 )
								ret := 0.000000
							if( marron_mean > 87.6392 )
								ret := -0.750000 // sell
					if( source > 25.5503 )
						if( verde_mean <= 79.3375 )
							if( nvimax <= 0.526203 )
								if( xmf <= 18.7643 )
									ret := 0.518519
								if( xmf > 18.7643 )
									ret := -0.117647
							if( nvimax > 0.526203 )
								if( tprice <= 365.822 )
									ret := -0.443366
								if( tprice > 365.822 )
									ret := 0.257143
						if( verde_mean > 79.3375 )
							if( marron <= 88.8191 )
								if( nvi_ema <= 0.64993 )
									ret := -0.108883
								if( nvi_ema > 0.64993 )
									ret := 0.230496
							if( marron > 88.8191 )
								if( marron_mean <= 71.9392 )
									ret := 0.352941
								if( marron_mean > 71.9392 )
									ret := -0.170294
				if( marron > 95.3242 )
					if( xrsi <= 80.7803 )
						if( verde_mean <= 171.994 )
							if( azul_mean <= -17.7784 )
								if( media_azul <= 141.049 )
									ret := -0.249412
								if( media_azul > 141.049 )
									ret := 0.311475
							if( azul_mean > -17.7784 )
								if( verde_azul <= 45.7913 )
									ret := -0.247423
								if( verde_azul > 45.7913 )
									ret := 0.041104
						if( verde_mean > 171.994 )
							if( verde_media <= 75.7232 )
								if( nvi <= -0.153986 )
									ret := 0.514286
								if( nvi > -0.153986 )
									ret := -0.163462
							if( verde_media > 75.7232 )
								if( verde_media <= 163.717 )
									ret := 0.441088
								if( verde_media > 163.717 )
									ret := -0.421053
					if( xrsi > 80.7803 )
						if( nvi <= 0.389768 )
							if( media_azul <= 79.1361 )
								if( marron <= 105.965 )
									ret := 1.000000 // buy
								if( marron > 105.965 )
									ret := -0.333333
							if( media_azul > 79.1361 )
								if( pvimax <= 0.957793 )
									ret := 0.167630
								if( pvimax > 0.957793 )
									ret := 0.596774
						if( nvi > 0.389768 )
							if( azul <= 42.0007 )
								if( source <= 52.0067 )
									ret := 0.555556
								if( source > 52.0067 )
									ret := -0.405910
							if( azul > 42.0007 )
								if( pvi_ema <= 0.919125 )
									ret := 0.552632
								if( pvi_ema > 0.919125 )
									ret := -0.204082
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Blai5_Koncorde_v10 
//@version=5
//indicator title="Koncorde v10", shorttitle="Konk_v5", overlay=false)

// Declare variables with explicit types
var float pvi = na
var float nvi = na

tprice = ohlc4
lengthEMA = input.int(255, minval=1)
m = input.int(15)
source = hlc3

// Pececillos
pvi := volume > volume[1] ? nz(pvi[1]) + (close - close[1]) / close[1] : nz(pvi[1])
pvim = ta.ema(pvi, m)
pvimax = ta.highest(pvim, 90)
pvimin = ta.lowest(pvim, 90)
oscp = (pvi - pvim) * 100 / (pvimax - pvimin)

// Tiburones
nvi := volume < volume[1] ? nz(nvi[1]) + (close - close[1]) / close[1] : nz(nvi[1])
nvim = ta.ema(nvi, m)
nvimax = ta.highest(nvim, 90)
nvimin = ta.lowest(nvim, 90)
azul = (nvi - nvim) * 100 / (nvimax - nvimin)

// // Money Flow Index
// Money Flow Index
source_positive = ta.change(source) > 0 ? source : 0
source_negative = ta.change(source) < 0 ? source : 0
upper_s = math.sum(volume * source_positive, 14)
lower_s = math.sum(volume * source_negative, 14)
// Custom Money Flow Index calculation
money_flow_ratio = upper_s / lower_s
xmf = 100 - (100 / (1 + money_flow_ratio))


// Bollinger
mult = input.float(2.0)
basis = ta.sma(tprice, 25)
dev = mult * ta.stdev(tprice, 25)
upper = basis + dev
lower = basis - dev
OB1 = (upper + lower) / 2.0
OB2 = upper - lower
BollOsc = (tprice - OB1) / OB2 * 100

xrsi = ta.rsi(tprice, 14)

// Stochastic Calculation Function
calc_stoch(src, length, smoothFastD) =>
    ll = ta.lowest(low, length)
    hh = ta.highest(high, length)
    k = 100 * (src - ll) / (hh - ll)
    ta.sma(k, smoothFastD)

stoc = calc_stoch(tprice, 21, 3)
marron = (xrsi + xmf + BollOsc + stoc / 3) / 2
verde = marron + oscp
media = ta.ema(marron, m)
bandacero = 0.0

azul_mean = ta.sma(azul, 5)
verde_mean = ta.sma(verde, 5)
marron_mean = ta.sma(marron, 5)
verde_azul = verde - azul
verde_media = verde - media
media_azul = media - azul
media_marron = media - marron
pvi_ema = pvim
nvi_ema = nvi

// PLOT
vl = plot(verde, color=color.new(#66FF66, 0), style=plot.style_area, title="verde")  // GREEN
ml = plot(marron, color=color.new(#FFCC99, 0), style=plot.style_area, title="marron")  // BEIGE
al = plot(azul, color=color.new(#00FFFF, 0), style=plot.style_area, title="azul")  // CYAN
plot(marron, color=color.new(#330000, 0), style=plot.style_line, linewidth=2, title="lmarron")  // DARK RED
plot(verde, color=color.new(#006600, 0), style=plot.style_line, linewidth=2, title="lineav")  // DARK GREEN
plot(azul, color=color.new(#000066, 0), style=plot.style_line, title="lazul")  // DARK BLUE
plot(media, color=color.new(#FF0000, 0), title="media", style=plot.style_line, linewidth=2)  // RED
plot(bandacero, color=color.new(#000000, 0), title="cero")  // BLACK

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
float op_operation = decision_tree_0_TWLO_15Min_baac7c86(nvi, nvi_ema, marron_mean, source, azul, verde_azul, verde_mean, xmf, pvimin, stoc, media, tprice, marron, pvim, pvimax, xrsi, oscp, pvi, nvimax, nvimin, verde, verde_media, azul_mean, nvim, BollOsc, pvi_ema, media_azul)

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


