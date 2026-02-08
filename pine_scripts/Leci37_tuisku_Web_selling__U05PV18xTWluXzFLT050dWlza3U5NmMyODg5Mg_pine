//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Blai5_Koncorde_v10
// ID_model: SNOW_1Min_1KON_96c28892 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SNOW_1Min_1KON_96c28892", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SNOW_1Min_96c28892(nvimin, azul, nvim, marron_mean, marron, nvimax, pvi, pvi_ema, oscp, verde, source, stoc, verde_mean, xrsi, media, xmf, tprice, pvimin, media_azul, verde_media, BollOsc, pvimax, nvi_ema, azul_mean, pvim, nvi, verde_azul)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8,max_features=sqrt, min_samples_leaf=7,random_state=843828734)
	if( pvi <= -0.044893 )
		if( xmf <= 10.5983 )
			if( nvi <= -0.049511 )
				if( verde_azul <= -22.1297 )
					if( tprice <= 125.62 )
						ret := 1.000000 // buy
					if( tprice > 125.62 )
						ret := 0.666667
				if( verde_azul > -22.1297 )
					if( media_azul <= 100.496 )
						if( pvimin <= -0.082433 )
							ret := -0.750000 // sell
						if( pvimin > -0.082433 )
							if( oscp <= 9.52634 )
								if( nvi <= -0.071221 )
									ret := -0.062500
								if( nvi > -0.071221 )
									ret := 0.157895
							if( oscp > 9.52634 )
								ret := 0.625000
					if( media_azul > 100.496 )
						ret := 1.000000 // buy
			if( nvi > -0.049511 )
				if( tprice <= 109.689 )
					if( source <= 108.918 )
						ret := -0.312500
					if( source > 108.918 )
						if( azul_mean <= -8.83078 )
							ret := 0.500000
						if( azul_mean > -8.83078 )
							if( verde_mean <= -29.2003 )
								ret := 1.000000 // buy
							if( verde_mean > -29.2003 )
								ret := 0.909091 // buy
				if( tprice > 109.689 )
					if( pvi_ema <= -0.18123 )
						if( BollOsc <= -60.993 )
							if( marron <= -13.9979 )
								if( media <= 13.4587 )
									ret := 1.000000 // buy
								if( media > 13.4587 )
									ret := 0.640000
							if( marron > -13.9979 )
								ret := 0.090909
						if( BollOsc > -60.993 )
							if( marron_mean <= -12.6281 )
								if( marron <= -17.9629 )
									ret := 1.000000 // buy
								if( marron > -17.9629 )
									ret := 0.363636
							if( marron_mean > -12.6281 )
								if( stoc <= 9.47408 )
									ret := -0.528455
								if( stoc > 9.47408 )
									ret := -0.147766
					if( pvi_ema > -0.18123 )
						if( verde_azul <= 12.257 )
							if( pvi <= -0.085066 )
								if( source <= 121.733 )
									ret := -0.882353 // sell
								if( source > 121.733 )
									ret := 0.080000
							if( pvi > -0.085066 )
								if( marron_mean <= -17.436 )
									ret := 0.214286
								if( marron_mean > -17.436 )
									ret := -0.643216
						if( verde_azul > 12.257 )
							if( marron <= 56.2697 )
								if( azul <= -60.7244 )
									ret := -0.535714
								if( azul > -60.7244 )
									ret := -0.905172 // sell
							if( marron > 56.2697 )
								ret := -0.181818
		if( xmf > 10.5983 )
			if( xrsi <= 46.5513 )
				if( marron_mean <= 5.5303 )
					if( BollOsc <= -50.8729 )
						if( xrsi <= 26.8782 )
							if( media_azul <= 51.8217 )
								if( pvimax <= -0.046613 )
									ret := 0.256125
								if( pvimax > -0.046613 )
									ret := -0.644444
							if( media_azul > 51.8217 )
								if( tprice <= 117.303 )
									ret := -0.746269 // sell
								if( tprice > 117.303 )
									ret := -0.175000
						if( xrsi > 26.8782 )
							if( xmf <= 28.6794 )
								if( nvim <= 0.190592 )
									ret := 0.835443 // buy
								if( nvim > 0.190592 )
									ret := 0.316667
							if( xmf > 28.6794 )
								if( stoc <= 7.95991 )
									ret := -0.900000 // sell
								if( stoc > 7.95991 )
									ret := 0.078947
					if( BollOsc > -50.8729 )
						if( media <= 20.1137 )
							if( tprice <= 114.813 )
								if( pvimax <= -0.414058 )
									ret := -0.112903
								if( pvimax > -0.414058 )
									ret := -0.668675
							if( tprice > 114.813 )
								if( stoc <= 18.5552 )
									ret := 0.035235
								if( stoc > 18.5552 )
									ret := -0.500000
						if( media > 20.1137 )
							if( tprice <= 130.933 )
								if( pvim <= -0.426092 )
									ret := 0.613636
								if( pvim > -0.426092 )
									ret := 0.078049
							if( tprice > 130.933 )
								if( verde_mean <= -23.3477 )
									ret := -0.647059
								if( verde_mean > -23.3477 )
									ret := -0.913043 // sell
				if( marron_mean > 5.5303 )
					if( media <= 30.839 )
						if( marron_mean <= 31.0254 )
							if( tprice <= 134.435 )
								if( nvi <= -0.023693 )
									ret := 0.204678
								if( nvi > -0.023693 )
									ret := 0.011403
							if( tprice > 134.435 )
								if( azul_mean <= -0.607391 )
									ret := -0.052941
								if( azul_mean > -0.607391 )
									ret := -0.587719
						if( marron_mean > 31.0254 )
							if( nvimax <= -0.026933 )
								if( azul_mean <= 35.8902 )
									ret := 0.265152
								if( azul_mean > 35.8902 )
									ret := -0.625000
							if( nvimax > -0.026933 )
								if( pvimin <= -0.445706 )
									ret := 0.215385
								if( pvimin > -0.445706 )
									ret := -0.393651
					if( media > 30.839 )
						if( azul <= 9.94631 )
							if( pvimax <= -0.444049 )
								if( pvimax <= -0.446543 )
									ret := 0.202520
								if( pvimax > -0.446543 )
									ret := 0.627907
							if( pvimax > -0.444049 )
								if( xmf <= 25.8339 )
									ret := 0.270017
								if( xmf > 25.8339 )
									ret := 0.066597
						if( azul > 9.94631 )
							if( oscp <= -11.6042 )
								if( tprice <= 109.479 )
									ret := 0.701493 // buy
								if( tprice > 109.479 )
									ret := 0.144016
							if( oscp > -11.6042 )
								if( nvimin <= 0.181702 )
									ret := 0.628975
								if( nvimin > 0.181702 )
									ret := 0.318471
			if( xrsi > 46.5513 )
				if( source <= 133.887 )
					if( media_azul <= 37.8368 )
						if( media <= 21.7198 )
							if( nvimin <= 0.010576 )
								ret := 0.384615
							if( nvimin > 0.010576 )
								if( pvi <= -0.218524 )
									ret := -0.939394 // sell
								if( pvi > -0.218524 )
									ret := -0.500000
						if( media > 21.7198 )
							if( verde_media <= 85.2779 )
								if( verde_azul <= -103.593 )
									ret := -0.607143
								if( verde_azul > -103.593 )
									ret := -0.102978
							if( verde_media > 85.2779 )
								if( oscp <= 44.4694 )
									ret := 0.906250 // buy
								if( oscp > 44.4694 )
									ret := 0.036145
					if( media_azul > 37.8368 )
						if( nvimax <= -0.03022 )
							if( verde <= 122.737 )
								if( tprice <= 130.537 )
									ret := 0.106903
								if( tprice > 130.537 )
									ret := -0.241563
							if( verde > 122.737 )
								if( nvi <= -0.078067 )
									ret := -0.158730
								if( nvi > -0.078067 )
									ret := 0.303644
						if( nvimax > -0.03022 )
							if( tprice <= 109.738 )
								if( media_azul <= 90.8994 )
									ret := 0.374046
								if( media_azul > 90.8994 )
									ret := -0.277778
							if( tprice > 109.738 )
								if( verde_azul <= 51.4164 )
									ret := 0.105456
								if( verde_azul > 51.4164 )
									ret := -0.043568
				if( source > 133.887 )
					if( verde_media <= -5.05889 )
						if( media <= 60.0739 )
							if( pvi_ema <= -0.068756 )
								if( media <= 48.8102 )
									ret := 1.000000 // buy
								if( media > 48.8102 )
									ret := 0.400000
							if( pvi_ema > -0.068756 )
								if( nvi <= -0.018046 )
									ret := 0.454545
								if( nvi > -0.018046 )
									ret := -0.294118
						if( media > 60.0739 )
							if( nvimax <= -0.010524 )
								if( verde_mean <= 68.9909 )
									ret := -0.585366
								if( verde_mean > 68.9909 )
									ret := 0.304348
							if( nvimax > -0.010524 )
								if( oscp <= 7.14637 )
									ret := -0.592233
								if( oscp > 7.14637 )
									ret := 0.400000
					if( verde_media > -5.05889 )
						if( nvi_ema <= 0.015395 )
							if( marron_mean <= 91.9971 )
								if( BollOsc <= -9.9216 )
									ret := 0.750000 // buy
								if( BollOsc > -9.9216 )
									ret := 0.098485
							if( marron_mean > 91.9971 )
								if( marron_mean <= 100.94 )
									ret := 0.753333 // buy
								if( marron_mean > 100.94 )
									ret := 0.438931
						if( nvi_ema > 0.015395 )
							if( tprice <= 135.223 )
								if( marron <= 106.178 )
									ret := 0.704918 // buy
								if( marron > 106.178 )
									ret := -0.200000
							if( tprice > 135.223 )
								if( tprice <= 138.125 )
									ret := -0.326923
								if( tprice > 138.125 )
									ret := -0.800000 // sell
	if( pvi > -0.044893 )
		if( media <= 93.4188 )
			if( xrsi <= 52.1308 )
				if( azul_mean <= 39.1487 )
					if( verde_azul <= 121.875 )
						if( source <= 146.164 )
							if( verde_azul <= 35.9852 )
								if( verde_media <= 3.95169 )
									ret := -0.100467
								if( verde_media > 3.95169 )
									ret := -0.460317
							if( verde_azul > 35.9852 )
								if( verde <= 21.1445 )
									ret := -0.229917
								if( verde > 21.1445 )
									ret := 0.090085
						if( source > 146.164 )
							if( azul_mean <= -51.7019 )
								if( oscp <= -26.4426 )
									ret := -0.897959 // sell
								if( oscp > -26.4426 )
									ret := -0.287234
							if( azul_mean > -51.7019 )
								if( nvi_ema <= -0.064258 )
									ret := -0.088998
								if( nvi_ema > -0.064258 )
									ret := 0.084512
					if( verde_azul > 121.875 )
						if( verde <= 88.2432 )
							if( media <= 46.5949 )
								if( xrsi <= 40.2114 )
									ret := 0.423077
								if( xrsi > 40.2114 )
									ret := 0.885714 // buy
							if( media > 46.5949 )
								if( azul <= -139.707 )
									ret := 0.843750 // buy
								if( azul > -139.707 )
									ret := 0.197368
						if( verde > 88.2432 )
							if( pvi <= 0.060653 )
								if( pvi <= 0.002698 )
									ret := 0.000000
								if( pvi > 0.002698 )
									ret := 0.627451
							if( pvi > 0.060653 )
								if( tprice <= 159.806 )
									ret := -0.543478
								if( tprice > 159.806 )
									ret := 0.270270
				if( azul_mean > 39.1487 )
					if( tprice <= 127.382 )
						if( media_azul <= -75.7201 )
							ret := -0.888889 // sell
						if( media_azul > -75.7201 )
							ret := -0.052632
					if( tprice > 127.382 )
						if( source <= 164.524 )
							if( nvi <= -0.01254 )
								if( oscp <= -15.4651 )
									ret := 0.802139 // buy
								if( oscp > -15.4651 )
									ret := 0.522727
							if( nvi > -0.01254 )
								if( xmf <= 24.9958 )
									ret := -0.600000
								if( xmf > 24.9958 )
									ret := 0.269231
						if( source > 164.524 )
							ret := -0.777778 // sell
			if( xrsi > 52.1308 )
				if( azul <= 41.8998 )
					if( pvi <= 0.155253 )
						if( BollOsc <= 10.3134 )
							if( azul <= -48.6337 )
								if( azul <= -56.2879 )
									ret := -1.000000 // sell
								if( azul > -56.2879 )
									ret := -0.812500 // sell
							if( azul > -48.6337 )
								if( media_azul <= 78.3582 )
									ret := -0.296890
								if( media_azul > 78.3582 )
									ret := 0.009940
						if( BollOsc > 10.3134 )
							if( azul_mean <= 43.1985 )
								if( nvi <= -0.029066 )
									ret := -0.082961
								if( nvi > -0.029066 )
									ret := 0.078082
							if( azul_mean > 43.1985 )
								if( nvimin <= -0.08819 )
									ret := -0.800000 // sell
								if( nvimin > -0.08819 )
									ret := 0.588889
					if( pvi > 0.155253 )
						if( azul_mean <= -6.21069 )
							ret := 0.521739
						if( azul_mean > -6.21069 )
							if( nvim <= -0.022604 )
								if( stoc <= 75.8123 )
									ret := -1.000000 // sell
								if( stoc > 75.8123 )
									ret := -0.906250 // sell
							if( nvim > -0.022604 )
								if( source <= 170.172 )
									ret := -0.043478
								if( source > 170.172 )
									ret := -0.837838 // sell
				if( azul > 41.8998 )
					if( pvimax <= 0.122029 )
						if( nvimax <= -0.04734 )
							if( pvimax <= 0.011266 )
								if( xmf <= 47.0999 )
									ret := 0.096774
								if( xmf > 47.0999 )
									ret := -0.550000
							if( pvimax > 0.011266 )
								if( oscp <= -19.2895 )
									ret := -0.361111
								if( oscp > -19.2895 )
									ret := 0.556962
						if( nvimax > -0.04734 )
							if( stoc <= 77.676 )
								if( stoc <= 76.3054 )
									ret := -0.401515
								if( stoc > 76.3054 )
									ret := 0.263158
							if( stoc > 77.676 )
								if( verde_azul <= 100.023 )
									ret := -0.639706
								if( verde_azul > 100.023 )
									ret := 0.333333
					if( pvimax > 0.122029 )
						if( verde_media <= -51.4066 )
							ret := -0.111111
						if( verde_media > -51.4066 )
							if( source <= 156.828 )
								ret := -0.181818
							if( source > 156.828 )
								if( azul_mean <= 56.007 )
									ret := -0.702703 // sell
								if( azul_mean > 56.007 )
									ret := -0.983871 // sell
		if( media > 93.4188 )
			if( pvi_ema <= 0.012695 )
				if( xrsi <= 63.9689 )
					if( oscp <= -8.15109 )
						if( pvi_ema <= -0.025053 )
							if( verde <= 68.2538 )
								if( nvimax <= -0.077495 )
									ret := -1.000000 // sell
								if( nvimax > -0.077495 )
									ret := -0.782609 // sell
							if( verde > 68.2538 )
								ret := -0.454545
						if( pvi_ema > -0.025053 )
							ret := -0.176471
					if( oscp > -8.15109 )
						if( pvimin <= -0.006629 )
							if( stoc <= 86.2741 )
								if( nvi_ema <= 0.007772 )
									ret := -0.187097
								if( nvi_ema > 0.007772 )
									ret := 0.625000
							if( stoc > 86.2741 )
								if( nvimax <= -0.05834 )
									ret := -0.400000
								if( nvimax > -0.05834 )
									ret := -0.900000 // sell
						if( pvimin > -0.006629 )
							ret := 0.629630
				if( xrsi > 63.9689 )
					if( xrsi <= 65.9188 )
						if( marron <= 106.654 )
							if( BollOsc <= 22.2111 )
								ret := 0.058824
							if( BollOsc > 22.2111 )
								if( media_azul <= 95.7957 )
									ret := 0.176471
								if( media_azul > 95.7957 )
									ret := 0.866667 // buy
						if( marron > 106.654 )
							ret := -0.153846
					if( xrsi > 65.9188 )
						if( nvi_ema <= -0.012078 )
							if( source <= 135.543 )
								if( oscp <= 25.2165 )
									ret := 0.060403
								if( oscp > 25.2165 )
									ret := -0.350318
							if( source > 135.543 )
								if( media_azul <= 80.7617 )
									ret := 0.737864 // buy
								if( media_azul > 80.7617 )
									ret := 0.082353
						if( nvi_ema > -0.012078 )
							if( BollOsc <= 49.4837 )
								if( nvi <= 0.019893 )
									ret := -0.282787
								if( nvi > 0.019893 )
									ret := -1.000000 // sell
							if( BollOsc > 49.4837 )
								if( verde_azul <= 112.377 )
									ret := 0.500000
								if( verde_azul > 112.377 )
									ret := 0.022222
			if( pvi_ema > 0.012695 )
				if( BollOsc <= 24.9235 )
					if( xrsi <= 58.8074 )
						if( source <= 160.938 )
							if( marron <= 73.5485 )
								if( tprice <= 159.096 )
									ret := 0.243243
								if( tprice > 159.096 )
									ret := -0.555556
							if( marron > 73.5485 )
								if( verde_azul <= 106.627 )
									ret := -0.857143 // sell
								if( verde_azul > 106.627 )
									ret := 0.000000
						if( source > 160.938 )
							if( nvimin <= -0.030909 )
								ret := 0.750000 // buy
							if( nvimin > -0.030909 )
								if( xmf <= 65.4387 )
									ret := 0.266667
								if( xmf > 65.4387 )
									ret := -0.500000
					if( xrsi > 58.8074 )
						if( source <= 157.14 )
							if( verde <= 74.2067 )
								ret := 0.809524 // buy
							if( verde > 74.2067 )
								if( BollOsc <= 24.4208 )
									ret := 0.057471
								if( BollOsc > 24.4208 )
									ret := 0.909091 // buy
						if( source > 157.14 )
							if( marron_mean <= 111.318 )
								if( marron <= 82.2028 )
									ret := -0.388889
								if( marron > 82.2028 )
									ret := 0.076190
							if( marron_mean > 111.318 )
								ret := -0.750000 // sell
				if( BollOsc > 24.9235 )
					if( azul_mean <= -22.2912 )
						if( azul <= -69.9254 )
							ret := -0.666667
						if( azul > -69.9254 )
							if( nvim <= -0.082705 )
								ret := 0.052632
							if( nvim > -0.082705 )
								if( nvi <= -0.064195 )
									ret := 1.000000 // buy
								if( nvi > -0.064195 )
									ret := 0.285714
					if( azul_mean > -22.2912 )
						if( xmf <= 49.296 )
							if( verde <= 101.342 )
								if( azul <= -1.9992 )
									ret := 1.000000 // buy
								if( azul > -1.9992 )
									ret := 0.750000 // buy
							if( verde > 101.342 )
								ret := 0.222222
						if( xmf > 49.296 )
							if( BollOsc <= 66.1845 )
								if( oscp <= 6.73026 )
									ret := -0.553444
								if( oscp > 6.73026 )
									ret := -0.290941
							if( BollOsc > 66.1845 )
								if( pvi_ema <= 0.099703 )
									ret := 0.724138 // buy
								if( pvi_ema > 0.099703 )
									ret := -0.277778
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
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
float op_operation = decision_tree_0_SNOW_1Min_96c28892(nvimin, azul, nvim, marron_mean, marron, nvimax, pvi, pvi_ema, oscp, verde, source, stoc, verde_mean, xrsi, media, xmf, tprice, pvimin, media_azul, verde_media, BollOsc, pvimax, nvi_ema, azul_mean, pvim, nvi, verde_azul)

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


