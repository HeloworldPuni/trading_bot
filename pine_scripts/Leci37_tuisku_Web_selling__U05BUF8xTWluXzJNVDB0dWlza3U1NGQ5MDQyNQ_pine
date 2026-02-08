//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Triple_EMA
// ID_model: SNAP_1Min_2MT0_54d90425 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SNAP_1Min_2MT0_54d90425", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SNAP_1Min_54d90425(Negative_Money_Flow_Sum, MFI_High, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Money_Flow_Ratio, Typical_Price, MFI, Positive_Money_Flow_Sum, Positive_Money_Flow, ema1, tema, ema12, ema2, ema3, ema13)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( Negative_Money_Flow <= 0.477409 )
		if( Money_Flow_Ratio <= 2.10849 )
			if( Positive_Money_Flow_Sum <= 980035 )
				if( ema12 <= -0.000924 )
					if( Negative_Money_Flow_Sum <= 151983 )
						if( ema12 <= -0.016758 )
							if( Raw_Money_Flow <= 6427.77 )
								if( ema2 <= 10.8609 )
									ret := 0.653846
								if( ema2 > 10.8609 )
									ret := 0.036364
							if( Raw_Money_Flow > 6427.77 )
								if( ema13 <= -0.042497 )
									ret := 0.849057 // buy
								if( ema13 > -0.042497 )
									ret := 0.457143
						if( ema12 > -0.016758 )
							if( tema <= 12.8726 )
								if( ema12 <= -0.003196 )
									ret := 0.288793
								if( ema12 > -0.003196 )
									ret := 0.043379
							if( tema > 12.8726 )
								if( Positive_Money_Flow <= 5848.42 )
									ret := 0.036496
								if( Positive_Money_Flow > 5848.42 )
									ret := -0.174797
					if( Negative_Money_Flow_Sum > 151983 )
						if( ema13 <= -0.000591 )
							if( MFI <= 66.6302 )
								if( Money_Flow_Ratio <= 0.571518 )
									ret := -0.073072
								if( Money_Flow_Ratio > 0.571518 )
									ret := -0.230769
							if( MFI > 66.6302 )
								ret := 1.000000 // buy
						if( ema13 > -0.000591 )
							if( ema3 <= 13.8555 )
								if( ema1 <= 11.6608 )
									ret := 0.370370
								if( ema1 > 11.6608 )
									ret := 0.913043 // buy
							if( ema3 > 13.8555 )
								if( Negative_Money_Flow_Sum <= 180918 )
									ret := -0.800000 // sell
								if( Negative_Money_Flow_Sum > 180918 )
									ret := 0.222222
				if( ema12 > -0.000924 )
					if( Positive_Money_Flow <= 332.902 )
						if( Positive_Money_Flow <= 288.986 )
							if( ema12 <= 0.009489 )
								if( ema12 <= 0.007316 )
									ret := -0.028886
								if( ema12 > 0.007316 )
									ret := 0.181818
							if( ema12 > 0.009489 )
								if( Positive_Money_Flow <= 28.6625 )
									ret := -0.201258
								if( Positive_Money_Flow > 28.6625 )
									ret := -1.000000 // sell
						if( Positive_Money_Flow > 288.986 )
							ret := 0.714286 // buy
					if( Positive_Money_Flow > 332.902 )
						if( Negative_Money_Flow_Sum <= 3.57364e+07 )
							if( Positive_Money_Flow <= 19607.2 )
								if( Typical_Price <= 11.6243 )
									ret := -0.196213
								if( Typical_Price > 11.6243 )
									ret := -0.331000
							if( Positive_Money_Flow > 19607.2 )
								if( ema13 <= 0.021637 )
									ret := -0.161746
								if( ema13 > 0.021637 )
									ret := 0.122995
						if( Negative_Money_Flow_Sum > 3.57364e+07 )
							if( Negative_Money_Flow_Sum <= 4.7133e+07 )
								if( Negative_Money_Flow_Sum <= 4.70992e+07 )
									ret := 0.166667
								if( Negative_Money_Flow_Sum > 4.70992e+07 )
									ret := 1.000000 // buy
							if( Negative_Money_Flow_Sum > 4.7133e+07 )
								if( Typical_Price <= 10.634 )
									ret := 0.166667
								if( Typical_Price > 10.634 )
									ret := -0.750000 // sell
			if( Positive_Money_Flow_Sum > 980035 )
				if( ema13 <= 0.05305 )
					if( ema13 <= -0.211376 )
						if( Negative_Money_Flow_Sum <= 2.38451e+07 )
							ret := 0.200000
						if( Negative_Money_Flow_Sum > 2.38451e+07 )
							if( ema13 <= -1.34492 )
								ret := 0.750000 // buy
							if( ema13 > -1.34492 )
								ret := 1.000000 // buy
					if( ema13 > -0.211376 )
						if( MFI <= 17.5924 )
							if( ema2 <= 15.1882 )
								if( Positive_Money_Flow_Sum <= 1.46473e+07 )
									ret := -0.366534
								if( Positive_Money_Flow_Sum > 1.46473e+07 )
									ret := 0.833333 // buy
							if( ema2 > 15.1882 )
								if( ema3 <= 16.4912 )
									ret := 0.213740
								if( ema3 > 16.4912 )
									ret := -0.590909
						if( MFI > 17.5924 )
							if( tema <= 11.1994 )
								if( Negative_Money_Flow_Sum <= 2.2173e+06 )
									ret := 0.071823
								if( Negative_Money_Flow_Sum > 2.2173e+06 )
									ret := -0.000569
							if( tema > 11.1994 )
								if( Negative_Money_Flow_Sum <= 2.90568e+06 )
									ret := 0.131610
								if( Negative_Money_Flow_Sum > 2.90568e+06 )
									ret := 0.047519
				if( ema13 > 0.05305 )
					if( Positive_Money_Flow <= 316837 )
						if( ema13 <= 0.092013 )
							if( Raw_Money_Flow <= 157896 )
								if( MFI <= 56.5638 )
									ret := -0.250000
								if( MFI > 56.5638 )
									ret := 0.166667
							if( Raw_Money_Flow > 157896 )
								if( MFI <= 63.6829 )
									ret := 0.650000
								if( MFI > 63.6829 )
									ret := 0.000000
						if( ema13 > 0.092013 )
							ret := -0.571429
					if( Positive_Money_Flow > 316837 )
						if( Raw_Money_Flow <= 2.01631e+06 )
							if( MFI_Low <= 42.9515 )
								if( MFI <= 38.6574 )
									ret := 0.400000
								if( MFI > 38.6574 )
									ret := -0.718447 // sell
							if( MFI_Low > 42.9515 )
								if( Positive_Money_Flow_Sum <= 6.18812e+06 )
									ret := 0.666667
								if( Positive_Money_Flow_Sum > 6.18812e+06 )
									ret := -0.382353
						if( Raw_Money_Flow > 2.01631e+06 )
							if( ema2 <= 14.4976 )
								if( ema3 <= 14.1143 )
									ret := -0.176471
								if( ema3 > 14.1143 )
									ret := 0.541667
							if( ema2 > 14.4976 )
								if( ema2 <= 15.09 )
									ret := -0.466667
								if( ema2 > 15.09 )
									ret := -1.000000 // sell
		if( Money_Flow_Ratio > 2.10849 )
			if( Negative_Money_Flow_Sum <= 383465 )
				if( Positive_Money_Flow <= 633.508 )
					if( ema13 <= 0.021717 )
						if( Positive_Money_Flow_Sum <= 3.91108e+07 )
							if( Typical_Price <= 15.6508 )
								if( Positive_Money_Flow_Sum <= 50473.4 )
									ret := -0.197531
								if( Positive_Money_Flow_Sum > 50473.4 )
									ret := 0.154589
							if( Typical_Price > 15.6508 )
								if( MFI_High <= -11.484 )
									ret := 0.750000 // buy
								if( MFI_High > -11.484 )
									ret := -0.238095
						if( Positive_Money_Flow_Sum > 3.91108e+07 )
							if( tema <= 12.3885 )
								if( Positive_Money_Flow_Sum <= 5.22162e+07 )
									ret := -0.933333 // sell
								if( Positive_Money_Flow_Sum > 5.22162e+07 )
									ret := -0.500000
							if( tema > 12.3885 )
								ret := 0.000000
					if( ema13 > 0.021717 )
						if( Positive_Money_Flow_Sum <= 181044 )
							if( Negative_Money_Flow_Sum <= 12224.1 )
								if( Positive_Money_Flow_Sum <= 45709.2 )
									ret := -0.307692
								if( Positive_Money_Flow_Sum > 45709.2 )
									ret := -0.850000 // sell
							if( Negative_Money_Flow_Sum > 12224.1 )
								if( MFI <= 68.5164 )
									ret := -1.000000 // sell
								if( MFI > 68.5164 )
									ret := -0.142857
						if( Positive_Money_Flow_Sum > 181044 )
							if( ema12 <= 0.027363 )
								if( Positive_Money_Flow_Sum <= 194020 )
									ret := 0.600000
								if( Positive_Money_Flow_Sum > 194020 )
									ret := 0.000000
							if( ema12 > 0.027363 )
								if( MFI <= 79.7462 )
									ret := -0.142857
								if( MFI > 79.7462 )
									ret := -1.000000 // sell
				if( Positive_Money_Flow > 633.508 )
					if( ema12 <= 0.03363 )
						if( ema12 <= 0.000942 )
							if( Negative_Money_Flow_Sum <= 331594 )
								if( ema12 <= -0.012315 )
									ret := 0.250000
								if( ema12 > -0.012315 )
									ret := -0.073741
							if( Negative_Money_Flow_Sum > 331594 )
								if( Raw_Money_Flow <= 67051.2 )
									ret := -0.916667 // sell
								if( Raw_Money_Flow > 67051.2 )
									ret := 0.000000
						if( ema12 > 0.000942 )
							if( Positive_Money_Flow <= 2.06118e+06 )
								if( Positive_Money_Flow_Sum <= 1.05615e+06 )
									ret := -0.291242
								if( Positive_Money_Flow_Sum > 1.05615e+06 )
									ret := -0.056641
							if( Positive_Money_Flow > 2.06118e+06 )
								if( Money_Flow_Ratio <= 23.3566 )
									ret := 0.200000
								if( Money_Flow_Ratio > 23.3566 )
									ret := -0.807018 // sell
					if( ema12 > 0.03363 )
						if( ema12 <= 0.066179 )
							if( Money_Flow_Ratio <= 110.881 )
								if( ema13 <= 0.110523 )
									ret := -0.669014
								if( ema13 > 0.110523 )
									ret := 0.400000
							if( Money_Flow_Ratio > 110.881 )
								if( Positive_Money_Flow_Sum <= 5.46801e+06 )
									ret := -1.000000 // sell
								if( Positive_Money_Flow_Sum > 5.46801e+06 )
									ret := 0.800000 // buy
						if( ema12 > 0.066179 )
							if( MFI <= 85.6305 )
								ret := -0.571429
							if( MFI > 85.6305 )
								if( ema12 <= 0.072928 )
									ret := -0.800000 // sell
								if( ema12 > 0.072928 )
									ret := -1.000000 // sell
			if( Negative_Money_Flow_Sum > 383465 )
				if( Negative_Money_Flow_Sum <= 7.5331e+06 )
					if( ema1 <= 9.07298 )
						if( Negative_Money_Flow_Sum <= 2.00652e+06 )
							if( Positive_Money_Flow_Sum <= 7.26043e+06 )
								if( Positive_Money_Flow <= 486039 )
									ret := -0.141304
								if( Positive_Money_Flow > 486039 )
									ret := 0.177778
							if( Positive_Money_Flow_Sum > 7.26043e+06 )
								if( tema <= 8.66049 )
									ret := 0.125000
								if( tema > 8.66049 )
									ret := -0.925926 // sell
						if( Negative_Money_Flow_Sum > 2.00652e+06 )
							if( ema13 <= -0.007664 )
								ret := 1.000000 // buy
							if( ema13 > -0.007664 )
								if( Positive_Money_Flow <= 459081 )
									ret := -0.703125 // sell
								if( Positive_Money_Flow > 459081 )
									ret := -0.313131
					if( ema1 > 9.07298 )
						if( ema2 <= 11.0345 )
							if( ema12 <= -0.022534 )
								ret := 1.000000 // buy
							if( ema12 > -0.022534 )
								if( MFI_Low <= 73.037 )
									ret := 0.061670
								if( MFI_Low > 73.037 )
									ret := -0.553191
						if( ema2 > 11.0345 )
							if( Negative_Money_Flow_Sum <= 1.39044e+06 )
								if( Positive_Money_Flow_Sum <= 9.86636e+06 )
									ret := -0.031618
								if( Positive_Money_Flow_Sum > 9.86636e+06 )
									ret := 0.366667
							if( Negative_Money_Flow_Sum > 1.39044e+06 )
								if( ema13 <= 0.093877 )
									ret := -0.122381
								if( ema13 > 0.093877 )
									ret := 0.149068
				if( Negative_Money_Flow_Sum > 7.5331e+06 )
					if( Raw_Money_Flow <= 3.12413e+06 )
						if( ema1 <= 8.73165 )
							ret := 1.000000 // buy
						if( ema1 > 8.73165 )
							if( ema12 <= 0.049584 )
								if( ema1 <= 13.9415 )
									ret := -0.560976
								if( ema1 > 13.9415 )
									ret := -0.127119
							if( ema12 > 0.049584 )
								if( Positive_Money_Flow <= 2.28492e+06 )
									ret := 0.000000
								if( Positive_Money_Flow > 2.28492e+06 )
									ret := 1.000000 // buy
					if( Raw_Money_Flow > 3.12413e+06 )
						if( ema2 <= 12.4057 )
							if( Positive_Money_Flow_Sum <= 5.15651e+07 )
								if( Positive_Money_Flow_Sum <= 3.54086e+07 )
									ret := -0.444444
								if( Positive_Money_Flow_Sum > 3.54086e+07 )
									ret := -1.000000 // sell
							if( Positive_Money_Flow_Sum > 5.15651e+07 )
								if( Typical_Price <= 11.6544 )
									ret := 0.750000 // buy
								if( Typical_Price > 11.6544 )
									ret := 1.000000 // buy
						if( ema2 > 12.4057 )
							if( MFI_High <= -10.9163 )
								if( MFI <= 68.0958 )
									ret := -1.000000 // sell
								if( MFI > 68.0958 )
									ret := 0.200000
							if( MFI_High > -10.9163 )
								if( Negative_Money_Flow_Sum <= 1.22334e+07 )
									ret := -0.672727
								if( Negative_Money_Flow_Sum > 1.22334e+07 )
									ret := -0.900000 // sell
	if( Negative_Money_Flow > 0.477409 )
		if( Positive_Money_Flow_Sum <= 151395 )
			if( ema12 <= -0.001303 )
				if( Raw_Money_Flow <= 3.11906e+06 )
					if( Negative_Money_Flow_Sum <= 172603 )
						if( ema12 <= -0.01887 )
							if( Negative_Money_Flow <= 13066.9 )
								if( Positive_Money_Flow_Sum <= 14986.5 )
									ret := 0.428571
								if( Positive_Money_Flow_Sum > 14986.5 )
									ret := 0.857143 // buy
							if( Negative_Money_Flow > 13066.9 )
								if( Raw_Money_Flow <= 29699.3 )
									ret := 0.035714
								if( Raw_Money_Flow > 29699.3 )
									ret := 0.800000 // buy
						if( ema12 > -0.01887 )
							if( Negative_Money_Flow <= 860.927 )
								if( Negative_Money_Flow_Sum <= 60457.6 )
									ret := 0.523810
								if( Negative_Money_Flow_Sum > 60457.6 )
									ret := 0.943662 // buy
							if( Negative_Money_Flow > 860.927 )
								if( Positive_Money_Flow_Sum <= 89018.4 )
									ret := 0.391765
								if( Positive_Money_Flow_Sum > 89018.4 )
									ret := 0.571429
					if( Negative_Money_Flow_Sum > 172603 )
						if( ema12 <= -0.052211 )
							if( ema2 <= 9.76654 )
								ret := 0.000000
							if( ema2 > 9.76654 )
								if( tema <= 16.4985 )
									ret := 0.952381 // buy
								if( tema > 16.4985 )
									ret := 0.250000
						if( ema12 > -0.052211 )
							if( ema13 <= -0.081049 )
								if( MFI_High <= -76.593 )
									ret := -0.900000 // sell
								if( MFI_High > -76.593 )
									ret := 0.000000
							if( ema13 > -0.081049 )
								if( Positive_Money_Flow <= 3175.82 )
									ret := 0.287474
								if( Positive_Money_Flow > 3175.82 )
									ret := 0.690476
				if( Raw_Money_Flow > 3.11906e+06 )
					if( Money_Flow_Ratio <= 0.001467 )
						if( Negative_Money_Flow_Sum <= 4.31279e+07 )
							ret := 0.000000
						if( Negative_Money_Flow_Sum > 4.31279e+07 )
							ret := 1.000000 // buy
					if( Money_Flow_Ratio > 0.001467 )
						if( ema13 <= -0.062901 )
							ret := -0.750000 // sell
						if( ema13 > -0.062901 )
							ret := -1.000000 // sell
			if( ema12 > -0.001303 )
				if( ema12 <= 0.009178 )
					if( Negative_Money_Flow <= 4507.06 )
						if( ema13 <= -0.005478 )
							if( Positive_Money_Flow <= 0.696168 )
								if( Typical_Price <= 14.4987 )
									ret := -0.666667
								if( Typical_Price > 14.4987 )
									ret := 0.333333
							if( Positive_Money_Flow > 0.696168 )
								ret := -1.000000 // sell
						if( ema13 > -0.005478 )
							if( Negative_Money_Flow_Sum <= 19265.3 )
								if( Negative_Money_Flow_Sum <= 6684.03 )
									ret := -0.058824
								if( Negative_Money_Flow_Sum > 6684.03 )
									ret := 0.605882
							if( Negative_Money_Flow_Sum > 19265.3 )
								if( Negative_Money_Flow_Sum <= 23984.7 )
									ret := -0.163934
								if( Negative_Money_Flow_Sum > 23984.7 )
									ret := 0.353459
					if( Negative_Money_Flow > 4507.06 )
						if( Negative_Money_Flow_Sum <= 27302.5 )
							if( ema1 <= 9.13399 )
								if( ema1 <= 9.00514 )
									ret := 0.000000
								if( ema1 > 9.00514 )
									ret := -0.333333
							if( ema1 > 9.13399 )
								if( Negative_Money_Flow <= 5488.57 )
									ret := 0.100000
								if( Negative_Money_Flow > 5488.57 )
									ret := 0.578125
						if( Negative_Money_Flow_Sum > 27302.5 )
							if( Positive_Money_Flow <= 23.6573 )
								if( Negative_Money_Flow_Sum <= 69148.3 )
									ret := 0.011976
								if( Negative_Money_Flow_Sum > 69148.3 )
									ret := 0.224324
							if( Positive_Money_Flow > 23.6573 )
								if( Positive_Money_Flow <= 9117.6 )
									ret := -0.588235
								if( Positive_Money_Flow > 9117.6 )
									ret := 0.600000
				if( ema12 > 0.009178 )
					if( Positive_Money_Flow_Sum <= 45401.3 )
						if( MFI <= 33.8935 )
							if( Money_Flow_Ratio <= 0.47583 )
								if( Negative_Money_Flow_Sum <= 60604 )
									ret := 0.400000
								if( Negative_Money_Flow_Sum > 60604 )
									ret := -0.240000
							if( Money_Flow_Ratio > 0.47583 )
								if( Money_Flow_Ratio <= 0.495304 )
									ret := 0.750000 // buy
								if( Money_Flow_Ratio > 0.495304 )
									ret := 1.000000 // buy
						if( MFI > 33.8935 )
							if( MFI_Low <= 41.949 )
								if( Negative_Money_Flow <= 604.313 )
									ret := 0.142857
								if( Negative_Money_Flow > 604.313 )
									ret := -0.677419
							if( MFI_Low > 41.949 )
								if( MFI_High <= -7.64196 )
									ret := 0.571429
								if( MFI_High > -7.64196 )
									ret := -0.125000
					if( Positive_Money_Flow_Sum > 45401.3 )
						if( ema12 <= 0.024606 )
							if( ema13 <= 0.026372 )
								if( Negative_Money_Flow <= 6414.55 )
									ret := 0.193333
								if( Negative_Money_Flow > 6414.55 )
									ret := -0.080645
							if( ema13 > 0.026372 )
								if( Raw_Money_Flow <= 1983.03 )
									ret := -0.105263
								if( Raw_Money_Flow > 1983.03 )
									ret := 0.429530
						if( ema12 > 0.024606 )
							if( Positive_Money_Flow_Sum <= 138893 )
								if( Positive_Money_Flow_Sum <= 72419.1 )
									ret := 0.533333
								if( Positive_Money_Flow_Sum > 72419.1 )
									ret := -0.634615
							if( Positive_Money_Flow_Sum > 138893 )
								if( MFI <= 65.9996 )
									ret := 1.000000 // buy
								if( MFI > 65.9996 )
									ret := 0.166667
		if( Positive_Money_Flow_Sum > 151395 )
			if( ema12 <= 0.009419 )
				if( Negative_Money_Flow_Sum <= 266834 )
					if( ema2 <= 13.8923 )
						if( ema12 <= -0.007332 )
							if( Money_Flow_Ratio <= 0.834268 )
								ret := -0.666667
							if( Money_Flow_Ratio > 0.834268 )
								if( Negative_Money_Flow <= 23235.5 )
									ret := 0.849206 // buy
								if( Negative_Money_Flow > 23235.5 )
									ret := 0.375000
						if( ema12 > -0.007332 )
							if( Negative_Money_Flow_Sum <= 57574.8 )
								if( Positive_Money_Flow <= 260.939 )
									ret := 0.094488
								if( Positive_Money_Flow > 260.939 )
									ret := -0.333333
							if( Negative_Money_Flow_Sum > 57574.8 )
								if( Positive_Money_Flow_Sum <= 298290 )
									ret := 0.308772
								if( Positive_Money_Flow_Sum > 298290 )
									ret := 0.607477
					if( ema2 > 13.8923 )
						if( Negative_Money_Flow <= 459.16 )
							if( Raw_Money_Flow <= 2845.83 )
								ret := -1.000000 // sell
							if( Raw_Money_Flow > 2845.83 )
								ret := 0.000000
						if( Negative_Money_Flow > 459.16 )
							if( ema13 <= -0.040203 )
								if( ema3 <= 15.2273 )
									ret := 0.500000
								if( ema3 > 15.2273 )
									ret := 0.916667 // buy
							if( ema13 > -0.040203 )
								if( ema3 <= 15.4715 )
									ret := 0.248344
								if( ema3 > 15.4715 )
									ret := 0.025090
				if( Negative_Money_Flow_Sum > 266834 )
					if( Negative_Money_Flow_Sum <= 1.30425e+07 )
						if( ema2 <= 16.8365 )
							if( MFI_High <= -10.0962 )
								if( ema12 <= -0.08904 )
									ret := 0.741935 // buy
								if( ema12 > -0.08904 )
									ret := 0.077579
							if( MFI_High > -10.0962 )
								if( MFI_Low <= 58.7285 )
									ret := -0.153226
								if( MFI_Low > 58.7285 )
									ret := 0.183333
						if( ema2 > 16.8365 )
							if( Money_Flow_Ratio <= 1.19631 )
								if( ema12 <= -0.042881 )
									ret := -0.960000 // sell
								if( ema12 > -0.042881 )
									ret := -0.185771
							if( Money_Flow_Ratio > 1.19631 )
								if( Raw_Money_Flow <= 498989 )
									ret := 0.565217
								if( Raw_Money_Flow > 498989 )
									ret := 0.055556
					if( Negative_Money_Flow_Sum > 1.30425e+07 )
						if( MFI_Low <= -12.9411 )
							if( Negative_Money_Flow <= 549086 )
								if( ema12 <= 0.004359 )
									ret := 0.226190
								if( ema12 > 0.004359 )
									ret := -0.857143 // sell
							if( Negative_Money_Flow > 549086 )
								if( Typical_Price <= 16.069 )
									ret := 0.964706 // buy
								if( Typical_Price > 16.069 )
									ret := 0.210526
						if( MFI_Low > -12.9411 )
							if( Money_Flow_Ratio <= 0.287704 )
								if( ema1 <= 16.2886 )
									ret := 0.096506
								if( ema1 > 16.2886 )
									ret := -0.409091
							if( Money_Flow_Ratio > 0.287704 )
								if( ema12 <= -0.059582 )
									ret := 0.684932
								if( ema12 > -0.059582 )
									ret := 0.214181
			if( ema12 > 0.009419 )
				if( Negative_Money_Flow_Sum <= 5.18759e+07 )
					if( Positive_Money_Flow_Sum <= 2.45598e+07 )
						if( Negative_Money_Flow_Sum <= 1.05428e+07 )
							if( Positive_Money_Flow_Sum <= 5.09929e+06 )
								if( ema12 <= 0.025366 )
									ret := -0.053165
								if( ema12 > 0.025366 )
									ret := -0.259861
							if( Positive_Money_Flow_Sum > 5.09929e+06 )
								if( ema3 <= 15.8638 )
									ret := 0.099671
								if( ema3 > 15.8638 )
									ret := -0.112875
						if( Negative_Money_Flow_Sum > 1.05428e+07 )
							if( tema <= 8.907 )
								ret := 1.000000 // buy
							if( tema > 8.907 )
								if( ema2 <= 14.6788 )
									ret := -0.475000
								if( ema2 > 14.6788 )
									ret := -0.067961
					if( Positive_Money_Flow_Sum > 2.45598e+07 )
						if( Typical_Price <= 14.5806 )
							if( Positive_Money_Flow_Sum <= 3.39413e+07 )
								if( Positive_Money_Flow_Sum <= 2.62947e+07 )
									ret := 0.076923
								if( Positive_Money_Flow_Sum > 2.62947e+07 )
									ret := 0.906667 // buy
							if( Positive_Money_Flow_Sum > 3.39413e+07 )
								if( Positive_Money_Flow <= 35967 )
									ret := -0.061538
								if( Positive_Money_Flow > 35967 )
									ret := 0.777778 // buy
						if( Typical_Price > 14.5806 )
							if( Positive_Money_Flow_Sum <= 2.85874e+07 )
								if( Raw_Money_Flow <= 1.33353e+06 )
									ret := -0.176471
								if( Raw_Money_Flow > 1.33353e+06 )
									ret := 0.659574
							if( Positive_Money_Flow_Sum > 2.85874e+07 )
								if( ema3 <= 14.7442 )
									ret := -0.735294 // sell
								if( ema3 > 14.7442 )
									ret := -0.058252
				if( Negative_Money_Flow_Sum > 5.18759e+07 )
					if( ema2 <= 14.3291 )
						ret := -1.000000 // sell
					if( ema2 > 14.3291 )
						ret := 0.250000
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Money_Flow_Index 
//@version=5
//indicator title="Money Flow Index (MFI)", shorttitle="MFI", format=format.price, precision=2, timeframe="", timeframe_gaps=true)

// Input parameters
length_MFI = input.int(14, minval=1, title="MFI Length")

// Calculate the Typical Price
Typical_Price = (high + low + close) / 3

// Calculate Raw Money Flow
Raw_Money_Flow = Typical_Price * volume

// Calculate Positive and Negative Money Flow
Positive_Money_Flow = Raw_Money_Flow * (Typical_Price > Typical_Price[1] ? 1 : 0)
Negative_Money_Flow = Raw_Money_Flow * (Typical_Price < Typical_Price[1] ? 1 : 0)

// Sum of Positive and Negative Money Flow over the given length
Positive_Money_Flow_Sum = ta.sma(Positive_Money_Flow, length_MFI) * length_MFI
Negative_Money_Flow_Sum = ta.sma(Negative_Money_Flow, length_MFI) * length_MFI

// Calculate Money Flow Ratio
Money_Flow_Ratio = Positive_Money_Flow_Sum / Negative_Money_Flow_Sum

// Calculate MFI
MFI = 100 - (100 / (1 + Money_Flow_Ratio))

// Calculate MFI high and low bands
MFI_High = MFI - 80
MFI_Low = MFI - 20

// Plot the MFI
plot(MFI, color=color.blue, title="MFI")

// Plot the MFI high and low bands
hline(80, "MFI High", color=color.red, linestyle=hline.style_dashed)
hline(20, "MFI Low", color=color.green, linestyle=hline.style_dashed)
plot(MFI_High, color=color.red, title="MFI High Band")
plot(MFI_Low, color=color.green, title="MFI Low Band")


//CODE associated with the technical indicator L_Triple_EMA 
//@version=5
//indicator title="Triple EMA", shorttitle="TEMA", overlay=true, timeframe="", timeframe_gaps=true)
length_TEMA = input.int(9, minval=1)
ema1 = ta.ema(close, length_TEMA)
ema2 = ta.ema(ema1, length_TEMA)
ema3 = ta.ema(ema2, length_TEMA)
tema = 3 * (ema1 - ema2) + ema3
plot(tema, "TEMA", color=#2962FF)

ema12 = ema1 - ema2
ema13 = ema1 - ema3


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
float op_operation = decision_tree_0_SNAP_1Min_54d90425(Negative_Money_Flow_Sum, MFI_High, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Money_Flow_Ratio, Typical_Price, MFI, Positive_Money_Flow_Sum, Positive_Money_Flow, ema1, tema, ema12, ema2, ema3, ema13)

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


