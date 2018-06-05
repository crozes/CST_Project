<?php
/**
 * @package td_esgat Template
 * @author joomlatd
 * @file-Main Component's Structure
 */

defined('_JEXEC') or die;
?>

		<div class="modspot">
		<div class="container clear">
        <jdoc:include type="message" />    
		<?php if (($this->countModules( 'left' ) ==0) AND ($this->countModules('right' ) ==0))
        { ?> 
        <!-- Without Sidebars -->		
        <div class="row">
            <div class="col-md-12">
                <?php if($this->countModules('maintop')) : ?>

            	<div class="mainspot"><jdoc:include type="modules" name="maintop" style="td_xhtml" /></div>

                <?php endif; ?>
                
                <jdoc:include type="component" />
                
				<?php if($this->countModules('mainbottom')) : ?>

            	<div class="mainspot"><jdoc:include type="modules" name="mainbottom" style="td_xhtml" /></div>

                <?php endif; ?>
            </div>
        </div>
        </div> <!--Container End -->
        </div> <!-- Modspot End -->
        <?php } ?>
                
		<?php if (($this->countModules( 'left' ) >=1) AND ($this->countModules('right' ) >=1))
        { ?> 
        <!-- With 2 Sidebars (Left & Right) -->
        <div class="row">
            <div class="col-md-3">
                <div class="sidebar">
                    <jdoc:include type="modules" name="left" style="td_xhtml" />
                </div>
            </div> 
            <div class="col-md-6">
            	<?php if($this->countModules('maintop')) : ?>

            	<div class="mainspot"><jdoc:include type="modules" name="maintop" style="td_xhtml" /></div>

                <?php endif; ?>

          		<div class="content"><jdoc:include type="component" /></div> <!-- Main Component -->

                <?php if($this->countModules('mainbottom')) : ?>

                <div class="mainspot"><jdoc:include type="modules" name="mainbottom" style="td_xhtml" /></div>

                <?php endif; ?>
            </div>
            <div class="col-md-3">
                <div class="sidebar">
                    <jdoc:include type="modules" name="right" style="td_xhtml" />
                </div>
            </div>
        </div>
        </div>
        </div>
        <?php } ?>
                
		<?php if (($this->countModules( 'left' ) >=1) AND ($this->countModules('right' ) ==0))
        { ?> 
        <!-- With Left Sidebar -->
        <div class="row">
            <div class="col-12 col-sm-12 col-md-3 col-lg-3">
                <div class="sidebar">
                    <jdoc:include type="modules" name="left" style="td_xhtml" />
                </div>
                <a href="https://www.facebook.com/clubdesauvetagetoulousain/" class="btn btn-lg btn-fb btn-social text-white" role="button"><i class="fab fa-facebook-f"></i> Facebook</a>
                <a href="#" class="btn btn-lg btn-inst btn-social text-white" role="button"><i class="fab fa-instagram" ></i></i> Instagram</a>
                <a href="https://eos.ffss.fr/" class="btn btn-lg btn-eos btn-social text-white" role="button"><i class="fas fa-ambulance"></i> EOS FFSS</a>
                <a href="mailto:cstsecretariat@live.fr" class="btn btn-lg btn-env btn-social text-white" role="button"><i class="far fa-envelope"></i> Email</a>
            </div>
            <div class="col-12 col-sm-12 col-md-9 col-lg-9">
            	<?php if($this->countModules('maintop')) : ?>

            	<div class="mainspot"><jdoc:include type="modules" name="maintop" style="td_xhtml" /></div>

                <?php endif; ?>
                
          		<div class="content"><jdoc:include type="component" /></div> <!-- Main Component -->
                
                <?php if($this->countModules('mainbottom')) : ?>

                <div class="mainspot"><jdoc:include type="modules" name="mainbottom" style="td_xhtml" /></div>

                <?php endif; ?>
                
            </div>
        </div>
        </div>
        </div>
        <?php } ?>
        
		<?php if (($this->countModules( 'left' ) ==0) AND ($this->countModules('right' ) >=1)) { ?>
        <!-- With Right Sidebar -->
        <div class="row">
            <div class="col-md-9">
            	<?php if($this->countModules('maintop')) : ?>

            	<div class="mainspot"><jdoc:include type="modules" name="maintop" style="td_xhtml" /></div>

                <?php endif; ?>
                
          		<div class="content"><jdoc:include type="component" /></div> <!-- Main Component -->
                
                <?php if($this->countModules('mainbottom')) : ?>

                <div class="mainspot"><jdoc:include type="modules" name="mainbottom" style="td_xhtml" /></div>

                <?php endif; ?>

            </div>      
            <div class="col-md-3">
                <div class="sidebar">
                    <jdoc:include type="modules" name="right" style="td_xhtml" />
                </div>
            </div>
        </div>
        </div>
        </div>
        <?php } ?>

