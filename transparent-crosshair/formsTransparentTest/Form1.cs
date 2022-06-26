using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace formsTransparentTest
{
    public partial class Form1 : Form
    {
        static NotifyIcon ikona;
        static MenuItem menu;

        public Form1()
        {
            InitializeComponent();
            InitializeIcon();

        }
        private void RedDot_Shown(object sender, EventArgs e)
        {
            this.AutoSize = false;
            this.BackColor = Color.Red;
            this.FormBorderStyle = FormBorderStyle.None;
            this.AllowTransparency = true;
            this.Opacity = 0.30;
            this.ShowInTaskbar = false;
            this.ShowIcon = true;
            this.StartPosition = FormStartPosition.Manual;
            this.DesktopLocation = new Point(1274, 715);
            this.Size = new Size(9, 9);
            this.TopMost = true;
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.TopMost = true;
        }

        static void InitializeIcon()
        {

            ikona = new NotifyIcon();
            ikona.Icon = new Icon("ikona.ico");
            ikona.ContextMenu = new ContextMenu(new[]
            {
                menu = new MenuItem("Wyjście", QuitClicked)
            });
            ikona.Visible = true;

        }
        static void QuitClicked(object o, EventArgs e)
        {
            Application.Exit();
            ikona.Dispose();
        }

        static void OnExit(object sender, EventArgs e)
        {
            ikona.Dispose();
        }
    }
}
