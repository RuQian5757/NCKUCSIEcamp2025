﻿namespace calculator
{
    partial class Form1
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置受控資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.button10 = new System.Windows.Forms.Button();
            this.button11 = new System.Windows.Forms.Button();
            this.button12 = new System.Windows.Forms.Button();
            this.button13 = new System.Windows.Forms.Button();
            this.button14 = new System.Windows.Forms.Button();
            this.button15 = new System.Windows.Forms.Button();
            this.button16 = new System.Windows.Forms.Button();
            this.button17 = new System.Windows.Forms.Button();
            this.button18 = new System.Windows.Forms.Button();
            this.button19 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.Font = new System.Drawing.Font("新細明體", 16F);
            this.label1.Location = new System.Drawing.Point(12, 21);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(310, 38);
            this.label1.TabIndex = 0;
            this.label1.Text = "label1";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(18, 139);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(70, 70);
            this.button1.TabIndex = 1;
            this.button1.Text = "1";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.Button_NumberClick);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(94, 139);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(70, 70);
            this.button2.TabIndex = 2;
            this.button2.Text = "2";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.Button_NumberClick);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(170, 139);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(70, 70);
            this.button3.TabIndex = 3;
            this.button3.Text = "3";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.Button_NumberClick);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(246, 139);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(70, 70);
            this.button4.TabIndex = 4;
            this.button4.Text = "/";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.Button_OperatorClick);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(246, 215);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(70, 70);
            this.button5.TabIndex = 8;
            this.button5.Text = "*";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.Button_OperatorClick);
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(170, 215);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(70, 70);
            this.button6.TabIndex = 7;
            this.button6.Text = "6";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.Button_NumberClick);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(94, 215);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(70, 70);
            this.button7.TabIndex = 6;
            this.button7.Text = "5";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.Button_NumberClick);
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(18, 215);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(70, 70);
            this.button8.TabIndex = 5;
            this.button8.Text = "4";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.Button_NumberClick);
            // 
            // button9
            // 
            this.button9.Location = new System.Drawing.Point(246, 291);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(70, 70);
            this.button9.TabIndex = 12;
            this.button9.Text = "-";
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.Button_OperatorClick);
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(170, 291);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(70, 70);
            this.button10.TabIndex = 11;
            this.button10.Text = "9";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.Button_NumberClick);
            // 
            // button11
            // 
            this.button11.Location = new System.Drawing.Point(94, 291);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(70, 70);
            this.button11.TabIndex = 10;
            this.button11.Text = "8";
            this.button11.UseVisualStyleBackColor = true;
            this.button11.Click += new System.EventHandler(this.Button_NumberClick);
            // 
            // button12
            // 
            this.button12.Location = new System.Drawing.Point(18, 291);
            this.button12.Name = "button12";
            this.button12.Size = new System.Drawing.Size(70, 70);
            this.button12.TabIndex = 9;
            this.button12.Text = "7";
            this.button12.UseVisualStyleBackColor = true;
            this.button12.Click += new System.EventHandler(this.Button_NumberClick);
            // 
            // button13
            // 
            this.button13.Location = new System.Drawing.Point(246, 367);
            this.button13.Name = "button13";
            this.button13.Size = new System.Drawing.Size(70, 70);
            this.button13.TabIndex = 16;
            this.button13.Text = "+";
            this.button13.UseVisualStyleBackColor = true;
            this.button13.Click += new System.EventHandler(this.Button_OperatorClick);
            // 
            // button14
            // 
            this.button14.Location = new System.Drawing.Point(170, 367);
            this.button14.Name = "button14";
            this.button14.Size = new System.Drawing.Size(70, 70);
            this.button14.TabIndex = 15;
            this.button14.Text = "=";
            this.button14.UseVisualStyleBackColor = true;
            this.button14.Click += new System.EventHandler(this.Button_OperatorClick);
            // 
            // button15
            // 
            this.button15.Location = new System.Drawing.Point(94, 367);
            this.button15.Name = "button15";
            this.button15.Size = new System.Drawing.Size(70, 70);
            this.button15.TabIndex = 14;
            this.button15.Text = "0";
            this.button15.UseVisualStyleBackColor = true;
            this.button15.Click += new System.EventHandler(this.Button_NumberClick);
            // 
            // button16
            // 
            this.button16.Location = new System.Drawing.Point(170, 63);
            this.button16.Name = "button16";
            this.button16.Size = new System.Drawing.Size(70, 70);
            this.button16.TabIndex = 13;
            this.button16.Text = "C";
            this.button16.UseVisualStyleBackColor = true;
            this.button16.Click += new System.EventHandler(this.button16_Click);
            // 
            // button17
            // 
            this.button17.Location = new System.Drawing.Point(18, 367);
            this.button17.Name = "button17";
            this.button17.Size = new System.Drawing.Size(70, 70);
            this.button17.TabIndex = 17;
            this.button17.Text = ".";
            this.button17.UseVisualStyleBackColor = true;
            this.button17.Click += new System.EventHandler(this.Button_NumberClick);
            // 
            // button18
            // 
            this.button18.Location = new System.Drawing.Point(246, 63);
            this.button18.Name = "button18";
            this.button18.Size = new System.Drawing.Size(70, 70);
            this.button18.TabIndex = 18;
            this.button18.Text = "⌫";
            this.button18.UseVisualStyleBackColor = true;
            this.button18.Click += new System.EventHandler(this.button18_Click);
            // 
            // button19
            // 
            this.button19.Location = new System.Drawing.Point(94, 62);
            this.button19.Name = "button19";
            this.button19.Size = new System.Drawing.Size(70, 70);
            this.button19.TabIndex = 19;
            this.button19.Text = "紀錄";
            this.button19.UseVisualStyleBackColor = true;
            this.button19.Click += new System.EventHandler(this.button19_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(334, 461);
            this.Controls.Add(this.button19);
            this.Controls.Add(this.button18);
            this.Controls.Add(this.button17);
            this.Controls.Add(this.button13);
            this.Controls.Add(this.button14);
            this.Controls.Add(this.button15);
            this.Controls.Add(this.button16);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.button10);
            this.Controls.Add(this.button11);
            this.Controls.Add(this.button12);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.label1);
            this.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Form1";
            this.Text = "計算機";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.Button button12;
        private System.Windows.Forms.Button button13;
        private System.Windows.Forms.Button button14;
        private System.Windows.Forms.Button button15;
        private System.Windows.Forms.Button button16;
        private System.Windows.Forms.Button button17;
        private System.Windows.Forms.Button button18;
        private System.Windows.Forms.Button button19;
    }
}

