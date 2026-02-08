//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: SuperTrend
// ID_model: PYPL_1Min_1SUP_1c9d8808 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_PYPL_1Min_1SUP_1c9d8808", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_PYPL_1Min_1c9d8808(dn1, trend, atr, atr2, buySignalInt, sellSignalInt, up1, up, dn)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( up1 <= 66.2677 )
		if( up <= 63.1575 )
			if( trend <= 0 )
				if( dn <= 61.4224 )
					if( up1 <= 60.8925 )
						if( dn <= 60.598 )
							if( dn1 <= 60.5323 )
								if( atr2 <= 0.025793 )
									ret := -0.357143
								if( atr2 > 0.025793 )
									ret := 0.431925
							if( dn1 > 60.5323 )
								ret := -0.882353 // sell
						if( dn > 60.598 )
							if( up1 <= 60.6434 )
								if( atr <= 0.047914 )
									ret := 0.777778 // buy
								if( atr > 0.047914 )
									ret := 1.000000 // buy
							if( up1 > 60.6434 )
								ret := 1.000000 // buy
					if( up1 > 60.8925 )
						if( dn <= 61.2829 )
							ret := 0.058824
						if( dn > 61.2829 )
							if( atr <= 0.095807 )
								ret := -1.000000 // sell
							if( atr > 0.095807 )
								ret := -0.384615
				if( dn > 61.4224 )
					if( up1 <= 62.2887 )
						if( atr <= 0.091444 )
							if( dn <= 61.6563 )
								ret := 0.500000
							if( dn > 61.6563 )
								if( atr <= 0.038339 )
									ret := 0.642857
								if( atr > 0.038339 )
									ret := 0.961538 // buy
						if( atr > 0.091444 )
							ret := 1.000000 // buy
					if( up1 > 62.2887 )
						if( up <= 62.5411 )
							ret := -0.153846
						if( up > 62.5411 )
							if( atr <= 0.08149 )
								ret := 0.357143
							if( atr > 0.08149 )
								ret := 0.894737 // buy
			if( trend > 0 )
				if( buySignalInt <= 0.5 )
					if( dn1 <= 62.5393 )
						if( dn1 <= 58.0421 )
							if( dn1 <= 57.8765 )
								if( dn <= 57.5047 )
									ret := 0.411043
								if( dn > 57.5047 )
									ret := -0.102190
							if( dn1 > 57.8765 )
								if( up1 <= 57.5786 )
									ret := 0.708791 // buy
								if( up1 > 57.5786 )
									ret := 0.051661
						if( dn1 > 58.0421 )
							if( up1 <= 61.9616 )
								if( up <= 57.6629 )
									ret := 0.436170
								if( up > 57.6629 )
									ret := -0.017276
							if( up1 > 61.9616 )
								if( up <= 62.2645 )
									ret := -0.268817
								if( up > 62.2645 )
									ret := 0.780488 // buy
					if( dn1 > 62.5393 )
						if( atr <= 0.515445 )
							if( up <= 62.1631 )
								if( atr2 <= 0.093974 )
									ret := -0.383459
								if( atr2 > 0.093974 )
									ret := 0.333793
							if( up > 62.1631 )
								if( dn <= 63.414 )
									ret := 0.090242
								if( dn > 63.414 )
									ret := -0.084337
						if( atr > 0.515445 )
							if( up1 <= 62.4861 )
								if( atr2 <= 1.86194 )
									ret := 0.941860 // buy
								if( atr2 > 1.86194 )
									ret := 0.153846
							if( up1 > 62.4861 )
								ret := -0.333333
				if( buySignalInt > 0.5 )
					if( up1 <= 58.2457 )
						if( atr <= 0.070287 )
							ret := 0.363636
						if( atr > 0.070287 )
							if( atr2 <= 0.087554 )
								ret := 0.928571 // buy
							if( atr2 > 0.087554 )
								ret := 0.818182 // buy
					if( up1 > 58.2457 )
						if( up1 <= 59.883 )
							if( up <= 59.1698 )
								if( dn <= 58.8457 )
									ret := -0.650000
								if( dn > 58.8457 )
									ret := 0.307692
							if( up > 59.1698 )
								if( dn <= 59.5283 )
									ret := -0.111111
								if( dn > 59.5283 )
									ret := -0.671233
						if( up1 > 59.883 )
							if( atr2 <= 0.056575 )
								if( atr2 <= 0.05108 )
									ret := 0.284091
								if( atr2 > 0.05108 )
									ret := 0.782609 // buy
							if( atr2 > 0.056575 )
								if( up1 <= 60.0608 )
									ret := 0.750000 // buy
								if( up1 > 60.0608 )
									ret := -0.398601
		if( up > 63.1575 )
			if( dn <= 66.7175 )
				if( trend <= 0 )
					if( up1 <= 63.5838 )
						if( up1 <= 63.3932 )
							if( atr2 <= 0.083911 )
								if( atr2 <= 0.046735 )
									ret := 0.850000 // buy
								if( atr2 > 0.046735 )
									ret := 1.000000 // buy
							if( atr2 > 0.083911 )
								ret := 0.642857
						if( up1 > 63.3932 )
							if( dn1 <= 63.8432 )
								ret := -0.650000
							if( dn1 > 63.8432 )
								ret := -1.000000 // sell
					if( up1 > 63.5838 )
						if( atr <= 0.039682 )
							ret := 0.473684
						if( atr > 0.039682 )
							if( dn1 <= 64.6568 )
								if( atr <= 0.081363 )
									ret := 0.900000 // buy
								if( atr > 0.081363 )
									ret := 0.333333
							if( dn1 > 64.6568 )
								if( atr <= 0.057773 )
									ret := 0.631579
								if( atr > 0.057773 )
									ret := 0.951807 // buy
				if( trend > 0 )
					if( dn1 <= 63.6101 )
						if( atr2 <= 0.051706 )
							if( dn1 <= 63.596 )
								if( up <= 63.346 )
									ret := -0.071742
								if( up > 63.346 )
									ret := -0.448718
							if( dn1 > 63.596 )
								if( up1 <= 63.3699 )
									ret := -0.777778 // sell
								if( up1 > 63.3699 )
									ret := 0.000000
						if( atr2 > 0.051706 )
							if( up <= 63.2089 )
								if( atr <= 0.051201 )
									ret := -0.333333
								if( atr > 0.051201 )
									ret := -0.737931 // sell
							if( up > 63.2089 )
								if( dn <= 63.5441 )
									ret := 0.076923
								if( dn > 63.5441 )
									ret := -0.678261
					if( dn1 > 63.6101 )
						if( up <= 64.8056 )
							if( dn <= 65.2551 )
								if( up1 <= 64.7466 )
									ret := -0.053931
								if( up1 > 64.7466 )
									ret := -0.300000
							if( dn > 65.2551 )
								if( atr <= 0.274248 )
									ret := -0.568720
								if( atr > 0.274248 )
									ret := -0.074074
						if( up > 64.8056 )
							if( atr2 <= 0.22231 )
								if( up <= 64.8305 )
									ret := 0.328358
								if( up > 64.8305 )
									ret := -0.025037
							if( atr2 > 0.22231 )
								if( up1 <= 65.0565 )
									ret := 0.931818 // buy
								if( up1 > 65.0565 )
									ret := 0.470588
			if( dn > 66.7175 )
				if( atr2 <= 0.146371 )
					if( dn1 <= 67.0464 )
						if( dn1 <= 67.0232 )
							if( atr2 <= 0.084754 )
								ret := -0.100000
							if( atr2 > 0.084754 )
								if( atr <= 0.111476 )
									ret := -0.868852 // sell
								if( atr > 0.111476 )
									ret := -0.568182
						if( dn1 > 67.0232 )
							ret := 0.111111
					if( dn1 > 67.0464 )
						ret := -1.000000 // sell
				if( atr2 > 0.146371 )
					if( up <= 66.1223 )
						if( dn1 <= 67.2369 )
							if( dn1 <= 66.823 )
								if( atr <= 0.154477 )
									ret := -1.000000 // sell
								if( atr > 0.154477 )
									ret := 0.333333
							if( dn1 > 66.823 )
								if( atr2 <= 0.209239 )
									ret := 0.728571 // buy
								if( atr2 > 0.209239 )
									ret := 0.100000
						if( dn1 > 67.2369 )
							if( dn <= 67.3187 )
								if( dn1 <= 67.301 )
									ret := -0.312500
								if( dn1 > 67.301 )
									ret := -0.857143 // sell
							if( dn > 67.3187 )
								if( atr2 <= 0.281645 )
									ret := 0.956522 // buy
								if( atr2 > 0.281645 )
									ret := -0.431818
					if( up > 66.1223 )
						if( atr <= 0.173637 )
							if( dn <= 67.1416 )
								if( dn1 <= 67.1514 )
									ret := -0.133333
								if( dn1 > 67.1514 )
									ret := 1.000000 // buy
							if( dn > 67.1416 )
								ret := -0.555556
						if( atr > 0.173637 )
							if( atr2 <= 0.18682 )
								if( dn <= 67.1641 )
									ret := -0.142857
								if( dn > 67.1641 )
									ret := -0.571429
							if( atr2 > 0.18682 )
								if( dn <= 67.9125 )
									ret := -1.000000 // sell
								if( dn > 67.9125 )
									ret := -0.857143 // sell
	if( up1 > 66.2677 )
		if( dn <= 67.1277 )
			if( up <= 66.7098 )
				if( dn1 <= 66.8892 )
					if( atr <= 0.062053 )
						if( dn1 <= 66.7964 )
							if( dn <= 66.7638 )
								if( atr2 <= 0.026998 )
									ret := 0.761905 // buy
								if( atr2 > 0.026998 )
									ret := -0.044248
							if( dn > 66.7638 )
								if( atr2 <= 0.058426 )
									ret := 0.928571 // buy
								if( atr2 > 0.058426 )
									ret := 1.000000 // buy
						if( dn1 > 66.7964 )
							if( dn <= 66.8265 )
								if( up <= 66.5198 )
									ret := -0.400000
								if( up > 66.5198 )
									ret := -0.888889 // sell
							if( dn > 66.8265 )
								if( atr <= 0.045234 )
									ret := 1.000000 // buy
								if( atr > 0.045234 )
									ret := -0.024390
					if( atr > 0.062053 )
						if( atr2 <= 0.074748 )
							if( atr <= 0.067056 )
								if( dn <= 66.7839 )
									ret := 0.200000
								if( dn > 66.7839 )
									ret := 0.800000 // buy
							if( atr > 0.067056 )
								if( dn <= 66.7352 )
									ret := 0.700000 // buy
								if( dn > 66.7352 )
									ret := 0.944444 // buy
						if( atr2 > 0.074748 )
							if( up <= 66.3629 )
								if( atr <= 0.087681 )
									ret := 0.848485 // buy
								if( atr > 0.087681 )
									ret := 0.272727
							if( up > 66.3629 )
								if( dn <= 66.8119 )
									ret := -0.333333
								if( dn > 66.8119 )
									ret := -0.636364
				if( dn1 > 66.8892 )
					if( atr <= 0.051559 )
						if( up1 <= 66.6857 )
							if( up1 <= 66.6091 )
								ret := 0.888889 // buy
							if( up1 > 66.6091 )
								if( atr2 <= 0.045167 )
									ret := 0.923077 // buy
								if( atr2 > 0.045167 )
									ret := 1.000000 // buy
						if( up1 > 66.6857 )
							ret := 0.636364
					if( atr > 0.051559 )
						if( atr2 <= 0.096376 )
							if( atr2 <= 0.085335 )
								if( up1 <= 66.5585 )
									ret := 0.088889
								if( up1 > 66.5585 )
									ret := 0.662983
							if( atr2 > 0.085335 )
								if( dn <= 67.0496 )
									ret := 0.957447 // buy
								if( dn > 67.0496 )
									ret := 0.650000
						if( atr2 > 0.096376 )
							ret := 0.133333
			if( up > 66.7098 )
				if( dn1 <= 67.0997 )
					if( up <= 66.8099 )
						if( dn <= 66.9975 )
							if( atr <= 0.041021 )
								if( up <= 66.772 )
									ret := 0.300000
								if( up > 66.772 )
									ret := 0.083333
							if( atr > 0.041021 )
								ret := 0.000000
						if( dn > 66.9975 )
							if( up <= 66.732 )
								if( atr <= 0.055325 )
									ret := -1.000000 // sell
								if( atr > 0.055325 )
									ret := 0.533333
							if( up > 66.732 )
								if( atr2 <= 0.056338 )
									ret := -0.240741
								if( atr2 > 0.056338 )
									ret := -0.714286 // sell
					if( up > 66.8099 )
						if( atr2 <= 0.046772 )
							if( dn1 <= 67.0643 )
								if( up1 <= 66.8198 )
									ret := 0.533333
								if( up1 > 66.8198 )
									ret := 0.758621 // buy
							if( dn1 > 67.0643 )
								if( atr <= 0.027305 )
									ret := 0.083333
								if( atr > 0.027305 )
									ret := 0.461538
						if( atr2 > 0.046772 )
							ret := -0.800000 // sell
				if( dn1 > 67.0997 )
					if( atr <= 0.049949 )
						if( up <= 66.9026 )
							if( dn1 <= 67.134 )
								if( dn1 <= 67.1225 )
									ret := -0.083333
								if( dn1 > 67.1225 )
									ret := 0.631579
							if( dn1 > 67.134 )
								ret := -0.888889 // sell
						if( up > 66.9026 )
							if( up <= 67.0015 )
								if( atr <= 0.034116 )
									ret := 0.818182 // buy
								if( atr > 0.034116 )
									ret := 1.000000 // buy
							if( up > 67.0015 )
								ret := 0.187500
					if( atr > 0.049949 )
						if( up <= 66.7737 )
							ret := 0.285714
						if( up > 66.7737 )
							ret := 0.875000 // buy
		if( dn > 67.1277 )
			if( sellSignalInt <= 0.5 )
				if( up <= 81.5489 )
					if( up1 <= 77.7368 )
						if( atr2 <= 0.288969 )
							if( dn <= 78.2841 )
								if( dn <= 75.0139 )
									ret := 0.009646
								if( dn > 75.0139 )
									ret := 0.097657
							if( dn > 78.2841 )
								if( atr <= 0.19921 )
									ret := 0.797203 // buy
								if( atr > 0.19921 )
									ret := -0.500000
						if( atr2 > 0.288969 )
							if( atr2 <= 0.506563 )
								if( up <= 68.8421 )
									ret := 0.677419
								if( up > 68.8421 )
									ret := 0.257384
							if( atr2 > 0.506563 )
								if( up <= 67.4555 )
									ret := 0.360000
								if( up > 67.4555 )
									ret := -0.312500
					if( up1 > 77.7368 )
						if( dn1 <= 81.998 )
							if( atr <= 0.208879 )
								if( atr2 <= 0.085201 )
									ret := -0.047139
								if( atr2 > 0.085201 )
									ret := 0.067936
							if( atr > 0.208879 )
								if( dn <= 79.8328 )
									ret := -0.808824 // sell
								if( dn > 79.8328 )
									ret := -0.155340
						if( dn1 > 81.998 )
							if( up <= 81.3252 )
								if( dn <= 82.0206 )
									ret := 1.000000 // buy
								if( dn > 82.0206 )
									ret := 0.266667
							if( up > 81.3252 )
								ret := -0.384615
				if( up > 81.5489 )
					if( dn <= 81.7537 )
						ret := -0.200000
					if( dn > 81.7537 )
						if( dn <= 81.7672 )
							if( atr <= 0.038971 )
								ret := -0.857143 // sell
							if( atr > 0.038971 )
								ret := -1.000000 // sell
						if( dn > 81.7672 )
							if( dn1 <= 81.7952 )
								ret := -0.111111
							if( dn1 > 81.7952 )
								if( atr2 <= 0.045129 )
									ret := -0.787234 // sell
								if( atr2 > 0.045129 )
									ret := -0.277778
			if( sellSignalInt > 0.5 )
				if( up1 <= 78.2689 )
					if( atr2 <= 0.120836 )
						if( atr2 <= 0.059356 )
							if( up1 <= 72.9259 )
								if( dn <= 69.3652 )
									ret := 0.789474 // buy
								if( dn > 69.3652 )
									ret := -0.089286
							if( up1 > 72.9259 )
								if( up1 <= 77.4614 )
									ret := 0.875000 // buy
								if( up1 > 77.4614 )
									ret := 0.000000
						if( atr2 > 0.059356 )
							if( dn1 <= 72.576 )
								if( atr2 <= 0.095899 )
									ret := 0.900000 // buy
								if( atr2 > 0.095899 )
									ret := 0.611111
							if( dn1 > 72.576 )
								if( atr2 <= 0.080226 )
									ret := 0.869565 // buy
								if( atr2 > 0.080226 )
									ret := 0.388889
					if( atr2 > 0.120836 )
						ret := -0.272727
				if( up1 > 78.2689 )
					if( dn <= 81.1938 )
						if( dn <= 80.4693 )
							if( up <= 79.2696 )
								ret := -0.538462
							if( up > 79.2696 )
								ret := 0.687500
						if( dn > 80.4693 )
							if( up <= 80.7473 )
								ret := -0.733333 // sell
							if( up > 80.7473 )
								ret := -0.500000
					if( dn > 81.1938 )
						ret := 1.000000 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator SuperTrend 
//@version=5
//indicator title="Supertrend", overlay=true, format=format.price, precision=2, timeframe="")

Periods = input.int(title="ATR Period", defval=10)
src = input.source(hl2, title="Source")
Multiplier = input.float(title="ATR Multiplier", step=0.1, defval=3.0)
changeATR = input.bool(title="Change ATR Calculation Method?", defval=true)
showsignals = input.bool(title="Show Buy/Sell Signals?", defval=true)
highlighting = input.bool(title="Highlighter On/Off?", defval=true)

atr2 = ta.sma(ta.tr, Periods)
atr = changeATR ? ta.atr(Periods) : atr2

up = src - (Multiplier * atr)
up1 = nz(up[1], up)
up := close[1] > up1 ? math.max(up, up1) : up

dn = src + (Multiplier * atr)
dn1 = nz(dn[1], dn)
dn := close[1] < dn1 ? math.min(dn, dn1) : dn

var trend = 1
trend := nz(trend[1], trend)
trend := trend == -1 and close > dn1 ? 1 : trend == 1 and close < up1 ? -1 : trend

upPlot = plot(trend == 1 ? up : na, title="Up Trend", style=plot.style_linebr, linewidth=2, color=color.green)
dnPlot = plot(trend == 1 ? na : dn, title="Down Trend", style=plot.style_linebr, linewidth=2, color=color.red)

buySignal = trend == 1 and trend[1] == -1
sellSignal = trend == -1 and trend[1] == 1

plotshape(buySignal, title="UpTrend Begins", location=location.absolute, style=shape.circle, size=size.tiny, color=color.green, textcolor=color.white)
plotshape(sellSignal, title="DownTrend Begins", location=location.absolute, style=shape.circle, size=size.tiny, color=color.red, textcolor=color.white)

plotshape(showsignals and buySignal, title="Buy", text="Buy", location=location.absolute, style=shape.labelup, size=size.tiny, color=color.green, textcolor=color.white)
plotshape(showsignals and sellSignal, title="Sell", text="Sell", location=location.absolute, style=shape.labeldown, size=size.tiny, color=color.red, textcolor=color.white)

mPlot = plot(ohlc4, title="", style=plot.style_circles, linewidth=1)

longFillColor = highlighting ? (trend == 1 ? color.new(color.green, 80) : color.new(color.white, 100)) : color.new(color.white, 100)
shortFillColor = highlighting ? (trend == -1 ? color.new(color.red, 80) : color.new(color.white, 100)) : color.new(color.white, 100)

fill(mPlot, upPlot, title="UpTrend Highlighter", color=longFillColor)
fill(mPlot, dnPlot, title="DownTrend Highlighter", color=shortFillColor)

alertcondition(buySignal, title="SuperTrend Buy", message="SuperTrend Buy!")
alertcondition(sellSignal, title="SuperTrend Sell", message="SuperTrend Sell!")
changeCond = trend != trend[1]
alertcondition(changeCond, title="SuperTrend Direction Change", message="SuperTrend has changed direction!")

buySignalInt = buySignal ? 1: 0   //Bool to int
sellSignalInt = sellSignal ? 1: 0   //Bool to int

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
float op_operation = decision_tree_0_PYPL_1Min_1c9d8808(dn1, trend, atr, atr2, buySignalInt, sellSignalInt, up1, up, dn)

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


