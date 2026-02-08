//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Stochastic_RSI
// ID_model: FFIV_30Min_2MS0_35fec3e4 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_FFIV_30Min_2MS0_35fec3e4", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_FFIV_30Min_35fec3e4(Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price, d, d_k, smoothK_k, k, rsi1, smoothD_d)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( Typical_Price <= 143.026 )
		if( Positive_Money_Flow <= 9.16777e+06 )
			if( Positive_Money_Flow_Sum <= 9.71709e+07 )
				if( Typical_Price <= 118.564 )
					if( MFI_High <= -13.6738 )
						if( smoothD_d <= 55.948 )
							ret := 0.135904
						if( smoothD_d > 55.948 )
							ret := 0.374702
					if( MFI_High > -13.6738 )
						if( Negative_Money_Flow_Sum <= 1.5968e+07 )
							ret := 0.387097
						if( Negative_Money_Flow_Sum > 1.5968e+07 )
							ret := -0.161458
				if( Typical_Price > 118.564 )
					if( rsi1 <= 11.0856 )
						if( Negative_Money_Flow_Sum <= 1.23599e+08 )
							ret := -0.146667
						if( Negative_Money_Flow_Sum > 1.23599e+08 )
							ret := -0.794118 // sell
					if( rsi1 > 11.0856 )
						if( Raw_Money_Flow <= 8.84307e+06 )
							ret := 0.051550
						if( Raw_Money_Flow > 8.84307e+06 )
							ret := 0.175325
			if( Positive_Money_Flow_Sum > 9.71709e+07 )
				if( d <= 96.4025 )
					if( d_k <= -5.2006 )
						if( Positive_Money_Flow_Sum <= 1.1682e+08 )
							ret := -0.163934
						if( Positive_Money_Flow_Sum > 1.1682e+08 )
							ret := 0.623762
					if( d_k > -5.2006 )
						if( MFI_High <= 8.18064 )
							ret := -0.297030
						if( MFI_High > 8.18064 )
							ret := 0.158333
				if( d > 96.4025 )
					if( Negative_Money_Flow_Sum <= 3.43959e+07 )
						if( Money_Flow_Ratio <= 3.96436 )
							ret := -1.000000 // sell
						if( Money_Flow_Ratio > 3.96436 )
							ret := 0.185185
					if( Negative_Money_Flow_Sum > 3.43959e+07 )
						if( MFI_Low <= 38.0927 )
							ret := -0.142857
						if( MFI_Low > 38.0927 )
							ret := 0.745763 // buy
		if( Positive_Money_Flow > 9.16777e+06 )
			if( rsi1 <= 29.8994 )
				if( Positive_Money_Flow <= 1.69354e+07 )
					if( smoothK_k <= 3.65842 )
						if( smoothD_d <= -2.08384 )
							ret := 0.000000
						if( smoothD_d > -2.08384 )
							ret := -0.952381 // sell
					if( smoothK_k > 3.65842 )
						if( Positive_Money_Flow_Sum <= 4.68201e+07 )
							ret := 0.513514
						if( Positive_Money_Flow_Sum > 4.68201e+07 )
							ret := -0.269231
				if( Positive_Money_Flow > 1.69354e+07 )
					if( MFI_Low <= 46.1035 )
						if( Positive_Money_Flow_Sum <= 3.85655e+07 )
							ret := 0.000000
						if( Positive_Money_Flow_Sum > 3.85655e+07 )
							ret := 0.790123 // buy
					if( MFI_Low > 46.1035 )
						ret := -0.750000 // sell
			if( rsi1 > 29.8994 )
				if( d <= 61.0682 )
					if( Positive_Money_Flow_Sum <= 4.88442e+07 )
						if( Negative_Money_Flow_Sum <= 2.23777e+07 )
							ret := 0.642857
						if( Negative_Money_Flow_Sum > 2.23777e+07 )
							ret := -0.060606
					if( Positive_Money_Flow_Sum > 4.88442e+07 )
						if( Raw_Money_Flow <= 5.07899e+07 )
							ret := -0.358407
						if( Raw_Money_Flow > 5.07899e+07 )
							ret := 0.319149
				if( d > 61.0682 )
					if( Typical_Price <= 104.14 )
						if( MFI_Low <= 43.8685 )
							ret := 0.731707 // buy
						if( MFI_Low > 43.8685 )
							ret := -0.062500
					if( Typical_Price > 104.14 )
						if( Typical_Price <= 129 )
							ret := -0.177852
						if( Typical_Price > 129 )
							ret := 0.112583
	if( Typical_Price > 143.026 )
		if( Positive_Money_Flow_Sum <= 6.17442e+07 )
			if( smoothD_d <= 22.687 )
				if( Raw_Money_Flow <= 201384 )
					if( Positive_Money_Flow_Sum <= 3.65656e+07 )
						if( Negative_Money_Flow_Sum <= 1.62829e+08 )
							ret := 0.617647
						if( Negative_Money_Flow_Sum > 1.62829e+08 )
							ret := -1.000000 // sell
					if( Positive_Money_Flow_Sum > 3.65656e+07 )
						if( smoothK_k <= 19.4802 )
							ret := -0.380952
						if( smoothK_k > 19.4802 )
							ret := 0.923077 // buy
				if( Raw_Money_Flow > 201384 )
					if( MFI_Low <= 50.3459 )
						if( Positive_Money_Flow_Sum <= 6.81967e+06 )
							ret := 0.332192
						if( Positive_Money_Flow_Sum > 6.81967e+06 )
							ret := 0.004502
					if( MFI_Low > 50.3459 )
						if( Positive_Money_Flow_Sum <= 3.61505e+07 )
							ret := 0.791045 // buy
						if( Positive_Money_Flow_Sum > 3.61505e+07 )
							ret := 0.277978
			if( smoothD_d > 22.687 )
				if( Positive_Money_Flow_Sum <= 7.35297e+06 )
					if( Negative_Money_Flow_Sum <= 6.1892e+07 )
						if( MFI_Low <= -10.0808 )
							ret := 0.343750
						if( MFI_Low > -10.0808 )
							ret := -0.474453
					if( Negative_Money_Flow_Sum > 6.1892e+07 )
						if( Negative_Money_Flow <= 5.93427e+06 )
							ret := -1.000000 // sell
						if( Negative_Money_Flow > 5.93427e+06 )
							ret := 0.800000 // buy
				if( Positive_Money_Flow_Sum > 7.35297e+06 )
					if( MFI <= 69.8269 )
						if( Positive_Money_Flow_Sum <= 5.68613e+07 )
							ret := -0.020796
						if( Positive_Money_Flow_Sum > 5.68613e+07 )
							ret := 0.192364
					if( MFI > 69.8269 )
						if( Positive_Money_Flow_Sum <= 5.26129e+07 )
							ret := -0.203523
						if( Positive_Money_Flow_Sum > 5.26129e+07 )
							ret := -0.008979
		if( Positive_Money_Flow_Sum > 6.17442e+07 )
			if( k <= 6.0447 )
				if( MFI <= 27.9147 )
					if( Typical_Price <= 192.891 )
						ret := -1.000000 // sell
					if( Typical_Price > 192.891 )
						ret := -0.200000
				if( MFI > 27.9147 )
					if( MFI <= 63.545 )
						if( Raw_Money_Flow <= 4.62579e+07 )
							ret := -0.022346
						if( Raw_Money_Flow > 4.62579e+07 )
							ret := -1.000000 // sell
					if( MFI > 63.545 )
						if( Negative_Money_Flow_Sum <= 3.56969e+07 )
							ret := -0.170213
						if( Negative_Money_Flow_Sum > 3.56969e+07 )
							ret := -0.621849
			if( k > 6.0447 )
				if( Positive_Money_Flow_Sum <= 7.08116e+07 )
					if( d_k <= -7.6897 )
						if( Raw_Money_Flow <= 2.1709e+07 )
							ret := -0.057348
						if( Raw_Money_Flow > 2.1709e+07 )
							ret := 0.567164
					if( d_k > -7.6897 )
						if( Negative_Money_Flow_Sum <= 2.42653e+07 )
							ret := -0.133648
						if( Negative_Money_Flow_Sum > 2.42653e+07 )
							ret := -0.331450
				if( Positive_Money_Flow_Sum > 7.08116e+07 )
					if( Negative_Money_Flow_Sum <= 1.38936e+08 )
						if( Negative_Money_Flow_Sum <= 5.36757e+07 )
							ret := -0.002142
						if( Negative_Money_Flow_Sum > 5.36757e+07 )
							ret := -0.242875
					if( Negative_Money_Flow_Sum > 1.38936e+08 )
						if( Typical_Price <= 201.804 )
							ret := 0.463840
						if( Typical_Price > 201.804 )
							ret := -0.666667
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
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


//CODE associated with the technical indicator L_Stochastic_RSI 
//@version=5
//indicator title="Stochastic RSI", shorttitle="Stoch RSI", format=format.price, precision=2, timeframe="", timeframe_gaps=true)
smoothK = input.int(3, "K", minval=1)
smoothD = input.int(3, "D", minval=1)
lengthRSI = input.int(14, "RSI Length", minval=1)
lengthStoch = input.int(14, "Stochastic Length", minval=1)
src = input(close, title="RSI Source")
rsi1 = ta.rsi(src, lengthRSI)
k = ta.sma(ta.stoch(rsi1, rsi1, rsi1, lengthStoch), smoothK)
d = ta.sma(k, smoothD)
plot(k, "K", color=#2962FF)
plot(d, "D", color=#FF6D00)

d_k = d - k
smoothD_d = d - smoothD
smoothK_k = k - smoothK

h0 = hline(80, "Upper Band", color=#787B86)
hline(50, "Middle Band", color=color.new(#787B86, 50))
h1 = hline(20, "Lower Band", color=#787B86)
fill(h0, h1, color=color.rgb(33, 150, 243, 90), title="Background")
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
float op_operation = decision_tree_0_FFIV_30Min_35fec3e4(Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price, d, d_k, smoothK_k, k, rsi1, smoothD_d)

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


